import os
import subprocess
import tempfile
import uuid
import graphviz
from IPython.display import display, Image, SVG
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from common import helper
from common import tool

compiler = 'iverilog'
script_run = '/content/cad4u/verilog/script.ys'
script_yosys = '/content/cad4u/verilog/yosys_command.sh'
netlistsvg_run = '/content/cad4u/verilog/netlistsvg/bin/netlistsvg.js'
SKIN_PATH='/content/cad4u/verilog/netlistsvg/lib/'

ext = '.v'

@magics_class
class VERILOGPlugin(Magics):
    
    def __init__(self, shell):
        super(VERILOGPlugin, self).__init__(shell)
        self.argparser = helper.get_argparser()
        self.already_install = False

    def updateInstall(self):
        list_dependecies = ["iverilog", "python3-cairosvg", "yosys", "verilator"]
        tool.install(list_dependecies, "Verilog")
        
    @staticmethod
    def compile(file_path, flags):
        args = [compiler, file_path + ext, "-o", file_path + ".out"]

        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            if flag == "<":
                break
            args.append(flag)
        
        subprocess.check_output(args, stderr=subprocess.STDOUT)

    def run_verilog(self, file_path):
        args = [file_path + ".out"]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
            
        helper.print_out(output)
    
    def process(self, args, out=False):
        output = subprocess.check_output(args, stderr=subprocess.STDOUT).decode('utf8')
        if (out):
            helper.print_out(output)
    
    def run_yosys(self, file_path, flag=""):
        if flag == "":
            args = ['yosys', "-Q", "-T", "-q", "-s", script_run]
        else:
            args = [script_yosys, flag]
        self.process(args)

        args = [netlistsvg_run, 'output.json', '--skin '+SKIN_PATH+'default.svg']
        self.process(args)

        args = ['cairosvg', 'out.svg', '-o code.pdf']
        self.process(args)

        # Print image
        display(SVG('/content/out.svg'))

    @cell_magic
    def verilog(self, line, cell):

        list_dependecies = ["iverilog", "python3-cairosvg", "yosys", "verilator"]

        colab = tool.Colab()
        
        colab.install(list_dependecies, "Verilog")
        colab.compile("iverilog", cell, "code.v", "code.out", line.split())
        colab.execute("code.out")
        
        '''
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ext, "w") as f:
                f.write(cell)
            try:
                self.compile(file_path, args)
                self.run_verilog(file_path)
            except subprocess.CalledProcessError as e:
                helper.print_out(e.output.decode("utf8"))
        '''
    @cell_magic
    def print_verilog(self, line, cell):

        if not self.already_install:
            self.already_install = True
            self.updateInstall()

        if "-top" not in line: 
            line = ""

        file_path = os.path.join('/content/code')
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.run_yosys(file_path, line)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def waveform(self, line, cell):

        if not self.already_install:
            self.already_install = True
            self.updateInstall()

        args = line.split()

        if len(args) > 0:
            name = args[0]
            if '.vcd' not in name:
                name += '.vcd'
        else:
            print("Name of file not exist! Please give the name.")
            print("Ex. \%\%waveform <name_file>.vcd")
            exit(0)
        
        import sys
        sys.path.insert(0,'.')
        from cad4u.verilog.vcd_parser.vcd_plotter import VcdPlotter

        op_dict = []
        sign_list = []
        time_begin = []
        time_end = []
        base = []
        flag_op_dict = False

        for l in cell.strip().split("\n"):
            l = l.split("#")[0]
            if l == '':
                continue
            if 'sign_list' not in l and 'op_dict' not in l:
                s = l.replace('=', '+=[') + ']'
                exec(s)
            else:
                if 'op_dict' in l:
                    flag_op_dict = True
                exec(l.replace('=', '+='))
        if flag_op_dict == False:
            op_dict = [[{}]]
            
        vcd_plt = VcdPlotter('/content/%s'%name)
        vcd_plt.show(op_dict, sign_list, time_begin[0], time_end[0], base[0])
