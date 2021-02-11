import os
import subprocess
import tempfile
import uuid
import graphviz
from IPython.display import display, Image
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from common import helper

compiler = 'iverilog'
yosys_run = '/content/cad4u/verilog/yosys'
script_run = '/content/cad4u/verilog/script.ys'
ext = '.v'

@magics_class
class VERILOGPlugin(Magics):
    
    def __init__(self, shell):
        super(VERILOGPlugin, self).__init__(shell)
        self.argparser = helper.get_argparser()
        self.already_install = False

    def updateInstall(self):
        print("Installing iverilog. Please wait... ", end="")
        args = ["sh", "/content/cad4u/verilog/update_install.sh"]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        #helper.print_out(output)
        print("done!")

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
    
    def run_yosys(self, file_path):
        args = [yosys_run, "-Q", "-T", "-q", "-s", script_run]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)

        # Printer dot
        display(Image(filename="/content/code.png"))

    @cell_magic
    def verilog(self, line, cell):

        if not self.already_install:
            self.already_install = True
            self.updateInstall()

        args = line.split()

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ext, "w") as f:
                f.write(cell)
            try:
                self.compile(file_path, args)
                self.run_verilog(file_path)
            except subprocess.CalledProcessError as e:
                helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def print_verilog(self, line, cell):

        if not self.already_install:
            self.already_install = True
            self.updateInstall()

        args = line.split()

        file_path = os.path.join('/content/code')
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.run_yosys(file_path)
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

        sign_list = []
        time_begin = []
        time_end = []
        base = []

        for l in cell.strip().split("\n"):
            l = l.split("#")[0]
            if l == '':
                continue
            if 'sign_list' not in l:
                s = l.replace('=', '+=[') + ']'
                exec(s)
            else:
                exec(l.replace('=', '+='))

        vcd_plt  = VcdPlotter('/content/%s'%name)
        vcd_plt.show(sign_list, time_begin[0], time_end[0], base[0])
