import os
import subprocess
import tempfile
import uuid

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
import ipywidgets as widgets
from IPython.display import display
from ipywidgets import *
from common import helper

ext = '.py'

@magics_class
class Gem5Plugin(Magics):
    
    def __init__(self, shell):
        super(Gem5Plugin, self).__init__(shell)
        self.argparser = helper.get_argparser()
        self.already_install = False
        #self.updateInstall()
    
    def updateInstall(self):
        print("Installing gem5 dependencies. Please wait... ", end="")
        args = ["sh", "/content/cad4u/valgrind/update_install.sh"]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        #helper.print_out(output)
        print("done!")
    
    def execution(self, args):
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)
    
    def print_out_gem5(self, out: str):
        out = out.replace("\n","")
        print(out)

    def run_gem5(self, file_path, args):

        arguments = ["sh", "/content/cad4u/gem5/execute.sh", args[0], file_path + ext]
        self.execution(arguments)

        if len(args) > 1:
            if 'all' in args[1:]:
                arguments = ["cat", "/content/m5out/stats.txt"]
                self.execution(arguments)
            else:
                print("---------- Begin Simulation Statistics ----------")
                for s in args[1:]:
                    arguments = ["sh", "/content/cad4u/gem5/statistic.sh", s]
                    output = subprocess.check_output(arguments, stderr=subprocess.STDOUT)
                    output = output.decode('utf8')
                    self.print_out_gem5(output)

    def output_gem5(self, data):
        if len(data['stats']) > 0:
            if 'all' in data['stats']:
                arguments = ["cat", "/content/m5out/stats.txt"]
                self.execution(arguments)
            else:
                print("---------- Begin Simulation Statistics ----------")
                for s in data['stats']:
                    arguments = ["sh", "/content/cad4u/gem5/statistic.sh", s]
                    output = subprocess.check_output(arguments, stderr=subprocess.STDOUT)
                    output = output.decode('utf8')
                    self.print_out_gem5(output)

    def view_scope(self, with_cache=False, binary="", stats=[]):
        bool_with_cache = with_cache
        data = {"arch":"X86","cpu":"Simple","clk":1.0,"size_l1":16,"assoc_l1":2,"latency_l1":16,
                "size_l2":256,"assoc_l2":8,"latency_l2":20,"memory":'DDR3_1600',
                "binary":binary, "stats": stats}

        def on_button_clicked(b):
            if b.name == 'simulate':
                b.button_style = 'danger'
                b.description = 'wait'
                #try:
                import sys
                sys.path.insert(0,'.')
                if bool_with_cache:
                    from cad4u.gem5.examples.two_level import cache_gem5
                    cache_gem5(data)
                else:
                    from cad4u.gem5.examples.simple import simple_gem5
                    simple_gem5(data)
                arguments = ["sh", "/content/cad4u/gem5/execute.sh", data['arch'], '/content/gem5_code.py']
                self.execution(arguments)
                self.output_gem5(data)
                #except:
                #print("erro!")
                b.button_style = 'success'
                b.description = "Start Simulate"

        def on_value_change(change):
            if change['owner'].name in data:
                data[change['owner'].name] = change['new']

        def create_Text(description="", button_style=""):
            return Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'))
        def create_expanded_button(id, description="", button_style="", disabled=False):
            btn = Button(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'), disabled=disabled)
            btn.name = id
            btn.on_click(on_button_clicked)
            return btn
        def create_Float(id, description="", button_style="", min=1, max=10, value=1, step=1):
            floatText = BoundedFloatText(description=description, button_style=button_style, layout=Layout(height='auto', width='auto'), min=min, max=max, value=value, step=step)
            floatText.name = id
            floatText.observe(on_value_change, names='value')
            return floatText
        def create_Dropdown(id, description="", disabled=False, options=[], value='1'):
            dropdown = Dropdown(description=description, layout=Layout(height='30px', width='auto'), value=value, options=options, disabled=disabled)
            dropdown.name = id
            dropdown.observe(on_value_change, names='value')
            return dropdown

        # create a 10x2 grid layout
        grid = GridspecLayout(2, 10)
        # fill it in with widgets
        grid[0,0] = create_Text("Architecture", "warning")
        grid[0,1] = create_Dropdown("arch", options=["X86","RISCV","ARM"], value="X86")
        grid[0,2] = create_Text("CPU", "warning")
        grid[0,3] = create_Dropdown("cpu", options=["Simple","In Order","Out Order"], value="Simple")
        grid[1,0] = create_Text("Clock (GHz)", "warning")
        grid[1,1] = create_Float("clk", value=1.0, min=0.2, max=5.0, step=0.1)
        grid[1,2] = create_Text("Memory", "warning")
        grid[1,3] = create_Dropdown("memory", options=['DDR3_1600','DDR4_2400'], value='DDR3_1600')

        opts = []
        for i in range(0,20):
            opts.append(2**i)

        if with_cache:
            gridCache = GridspecLayout(3, 10)
            gridCache[0,0] = create_Text("Cache", "warning")
            gridCache[0,1] = create_Text("Size (kB)", "warning")
            gridCache[0,2] = create_Text("Associative", "warning")
            gridCache[0,3] = create_Text("data_latency", "warning")
            gridCache[1,0] = create_Text("L1Cache", "warning")
            gridCache[1,1] = create_Dropdown("size_l1", options=opts[:10], value=16)
            gridCache[1,2] = create_Dropdown("assoc_l1", options=opts[:5], value=2)
            gridCache[1,3] = create_Dropdown("latency_l1", options=range(14,28), value=16)
            gridCache[2,0] = create_Text("L2Cache", "warning")
            gridCache[2,1] = create_Dropdown("size_l2", options=opts[6:15], value=256)
            gridCache[2,2] = create_Dropdown("assoc_l2", options=opts[2:10], value=8)
            gridCache[2,3] = create_Dropdown("latency_l2", options=range(20,41), value=20)

        gridSim = GridspecLayout(1, 5)
        gridSim[0,0] = create_expanded_button("simulate", "Start Simulate", "success")

        display(grid)
        if with_cache:
            display(gridCache)
        display(gridSim)
    
    @cell_magic
    def gem5(self, line, cell):
        if not self.already_install:
            self.already_install = True
            self.updateInstall()
        args = line.split()

        file_path = '/content/gem5_code'

        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.run_gem5(file_path, args)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))

    @cell_magic
    def gem5_visual_simple(self, line, cell):
        if not self.already_install:
            self.already_install = True
            self.updateInstall()
        path_binary = []
        statistics = []

        for l in cell.strip().split("\n"):
            l = l.split("#")[0]
            if l == '':
                continue
            if 'statistics' not in l:
                s = l.replace('=', '+=[') + ']'
                exec(s)
            else:
                exec(l.replace('=', '+='))

        self.view_scope(with_cache=False, binary=path_binary[0], stats=statistics)
    
    @cell_magic
    def gem5_visual_cache(self, line, cell):
        if not self.already_install:
            self.already_install = True
            self.updateInstall()
        path_binary = []
        statistics = []

        for l in cell.strip().split("\n"):
            l = l.split("#")[0]
            if l == '':
                continue
            if 'statistics' not in l:
                s = l.replace('=', '+=[') + ']'
                exec(s)
            else:
                exec(l.replace('=', '+='))

        self.view_scope(with_cache=True, binary=path_binary[0], stats=statistics)
