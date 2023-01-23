import os
import subprocess
import tempfile
import uuid
from ipywidgets import *
from IPython.display import display

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from common import helper
from common import tool

compiler = '/usr/bin/g++'
ext = '.cpp'

@magics_class
class ValgrindPlugin(Magics):
    
    def __init__(self, shell):
        super(ValgrindPlugin, self).__init__(shell)
        self.argparser = helper.get_argparser()
        self.already_install = False
    
    def updateInstall(self):
        list_dependecies = ["valgrind"]
        if not self.already_install:
            self.already_install = True
            tool.install(list_dependecies)
    
    def parse_out(self, out, print_file):
        c = 0
        if print_file:
            f = open("/content/print_out.txt", "w")

        for l in out.split('\n'):
            if c > 12:
                res = l.split("==")
                if len(res) > 1:
                    print(res[2][1:])
                    if print_file:
                        f.write(res[2][1:] + "\n")
            c += 1
    
    def parse_res(self, out, results):
        c = 0
        for l in out.split('\n'):
            if c > 12:
                res = l.split("==")
                if len(res) > 1:
                    if 'D1  misses:' in res[2][1:]:
                        value = res[2][1:].split(":")[1].split("(")[0].replace(",","").replace(" ","")
                        if 'misses' in results:
                            results['misses'].append(int(value))
                    elif 'D1  miss rate:' in res[2][1:]:
                        value = res[2][1:].split(":")[1].split("(")[0].replace(",","").replace("%","").replace(" ","")
                        if 'miss_rate' in results:
                            results['miss_rate'].append(float(value))
            c += 1

    def exec_range_cache(self, args, results):

        v = '--D1=%d,%d,%d' %(args[0]*1024,args[1],args[2])
        args = ["sh", "/content/cad4u/valgrind/execute.sh", v, '', '']

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')

        self.parse_res(output, results)

    def executeValgrind(self, args, print_file):

        v = ['', '', '']

        for i in range(len(args)):
            if i >= 3:
                break
            v[i] = args[i]

        args = ["sh", "/content/cad4u/valgrind/execute.sh", v[0], v[1], v[2]]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')

        self.parse_out(output, print_file)
    
    def compile(self, file_path):
        args = [compiler, file_path + ext, "-o", file_path + ".out"]
        subprocess.check_output(args, stderr=subprocess.STDOUT)

    def run_cpp(self, file_path):
        
        self.compile(file_path)
        args = [file_path + ".out"]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
            
        helper.print_out(output)

    def print_bar(self, datacache, results):

        import matplotlib.pyplot as plt 

        labels = []
        for d in datacache:
            labels.append(str(d)+"kB")

        for r in results:
            fig, ax = plt.subplots()
            ax.set_xlabel("Size")
            if r == 'misses':
                ax.set_title('DataCache Misses')
                ax.bar(labels, results[r])
                ax.set_ylabel("D1 misses")
                plt.savefig("misses.svg")
            elif r == 'miss_rate':
                ax.set_title('DataCache Miss Rate')
                ax.bar(labels, results[r], color='g')
                ax.set_ylabel("D1 miss rate (%)")
                plt.savefig("miss_rate.svg")

    @cell_magic
    def cachegrind(self, line, cell):

        if not self.already_install:
            self.already_install = True
            self.updateInstall()

        print_file = False
        if '--file' in line:
            line.replace("--file", "")
            print_file = True

        args = line.split()

        file_path = '/content/valgrind_code'

        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.run_cpp(file_path)
            self.executeValgrind(args, print_file)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def rangecachegrind(self, line, cell):

        if not self.already_install:
            self.already_install = True
            self.updateInstall()

        datacache = [4]
        ways = [2]
        lines = [32]
        bargraph = ['misses', 'miss_rate']

        line = line.strip().replace(" ","").split(";")

        for l in line:
            if 'datacache' in l:
                datacache = []
                l = l.replace('datacache=','').replace('(','').replace(')','').split(',')
                for d in l:
                    datacache.append(int(d))
            elif 'ways' in l:
                ways = []
                l = l.replace('ways=','').replace('(','').replace(')','').split(',')
                for d in l:
                    ways.append(int(d))
            elif 'line' in l:
                lines = []
                l = l.replace('line=','').replace('(','').replace(')','').split(',')
                for d in l:
                    lines.append(int(d))
            elif 'bargraph' in l:
                bargraph = []
                l = l.replace('bargraph=','').replace('(','').replace(')','').split(',')
                for d in l:
                    bargraph.append(d)      

        file_path = '/content/valgrind_code'

        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.run_cpp(file_path)
            
            results = {}
            for b in bargraph:
                results[b] = []

            for i in range(len(datacache)):
                for j in range(len(ways)):
                    for k in range(len(lines)):
                        args = [datacache[i], ways[j], lines[k]]
                        self.exec_range_cache(args, results)
            self.print_bar(datacache, results)

        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
    
    size, assoc, lines, cache = 0, 0, 0, ''
    def create_visual(self, c):
        global size, assoc, lines, cache
        size, assoc, lines = 1, 2, 32
        cache = c

        def on_button_clicked(b):
            global size, assoc, lines, cache
            if b.name == 'exec':
                b.button_style = 'danger'
                b.description = 'wait'
                if cache == 'data':
                    exec = "--D1=%d,%d,%d" %(size*1024,assoc,lines)
                elif cache == 'inst':
                    exec = "--I1=%d,%d,%d" %(size*1024,assoc,lines)
                print("Parameters: %d, %d, %d\n" %(size*1024,assoc,lines))
                try:
                    self.executeValgrind([exec],True)
                except:
                    print("invalid parameters!")
                print("--" * 30) 
                b.button_style = 'success'
                b.description = "Start Simulate"

        def on_value_change(change):
            global size, assoc, lines
            if change['owner'].name == 'size':
                size = int(change['owner'].options[change['owner'].index])
            elif change['owner'].name == 'assoc':
                assoc = int(change['owner'].options[change['owner'].index])
            elif change['owner'].name == 'lines':
                lines = int(change['owner'].options[change['owner'].index])

        def create_Text(description="", button_style=""):
            return Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'))

        def create_Dropdown(id, description="", options=[], value='1'):
            dropdown = Dropdown(description=description, layout=Layout(height='30px', width='auto'), value=value, options=options)
            dropdown.name = id
            dropdown.observe(on_value_change, names='value')
            return dropdown

        def create_button(id, description="", button_style=""):
            btn = Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'))
            btn.name = id
            btn.on_click(on_button_clicked)
            return btn

        # create grid layout
        grid = GridspecLayout(1, 5)
        if cache == 'data':
            grid[0,0] = create_Text("Data Cache", "warning")
        elif cache == 'inst':
            grid[0,0] = create_Text("Instruction Cache", "warning")
        display(grid)

        grid = GridspecLayout(3, 10)
        grid[0,0] = create_Text("Size (kB)", "warning")
        opt = []
        for i in range(0,11):
            opt.append(2**i)
        grid[0,1] = create_Dropdown("size", options=opt, value=1)
        grid[1,0] = create_Text("Associative", "warning")
        grid[1,1] = create_Dropdown("assoc", options=opt[:6], value=2)
        grid[2,0] = create_Text("Line (Bytes)", "warning")
        opt = []
        for i in range(0,3):
            opt.append(32*(2**i))
        grid[2,1] = create_Dropdown("lines", options=opt, value=32)

        grid_exec = GridspecLayout(1, 5)
        grid_exec[0,0] = create_button("exec", "Start Execution", "success")

        display(grid)
        display(grid_exec)

    @cell_magic
    def datacache(self, flag, cell):

        colab = tool.Colab()        
        colab.install(["valgrind"])
        colab.compile("g++", cell, "code.cpp", "code.out")
        
        colab.grid(5)
        colab.text("Data Cache")
        colab.dropdown("size", "Size (kB)", [1,2,4,8,16])
        colab.dropdown("assoc", "Associative", [1,2,4,8,16,32])
        colab.dropdown("lines", "Line (Bytes)", [32, 64, 128])

        colab.exec("valgrind", "code.out", "--D1=")
        colab.show()
    
    @cell_magic
    def instructioncache(self, line, cell):
        if not self.already_install:
            self.already_install = True
            self.updateInstall()
        
        file_path = '/content/valgrind_code'

        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.run_cpp(file_path)
            self.create_visual('inst')
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
