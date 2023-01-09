import subprocess
import argparse

from IPython.display import display, Image, SVG
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

already_install = False

class Colab():
    
    def print_out(self, out: str):
        for l in out.split('\n'):
            print(l)

    def install(self, list):
        global already_install
        if not already_install:
            already_install = True
            print("Installing. Please wait... ", end="")
            output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT) 
            try:
                output = subprocess.check_output(["apt", "install"] + list, stderr=subprocess.STDOUT) 
                output = output.decode('utf8')
                print("done!")
            except subprocess.CalledProcessError as e:
                self.print_out(e.output.decode("utf8"))
                print("failed!")
    
    def compile(self, compiler, cell, file_path, file_output, flags):

        args = [compiler, file_path, "-o", file_output]

        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            if flag == "<":
                break
            args.append(flag)

        with open("/content/"+file_path, "w") as f:
            f.write(cell)
        try:
            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode('utf8') 
        except subprocess.CalledProcessError as e:
            self.print_out(e.output.decode("utf8"))
    
    def execute(self, file_path, print_output=True):

        args = ["/content/"+file_path]

        try:
            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode('utf8')
            self.print_out(out)
        except subprocess.CalledProcessError as e:
            self.print_out(e.out.decode("utf8"))
    
    def command_line(self, command, print_output=False):
        out = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode('utf8')
        if (print_output):
            self.print_out(out)
        return out

    def print_cfg(self, command):
        out = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT)
        for l in out.split("\n"):
            if "Writing" in l:
                name = l.split(" ")[1].replace("'","").replace("...","")
                self.command_line("dot -Tpng "+name+" -o /content/"+name+".png")
                self.display_png("/content/"+name+".png")
                
    def display_png(self, file_path):
        if ".png" not in file_path:
            file_path += ".png"
        display(filename="/content"+file_path)

    def display_svg(self, file_path):
        if ".svg" not in file_path:
            file_path += ".svg" 
        display(SVG('/content/'+file_path))