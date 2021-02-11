import os
import subprocess
import tempfile
import uuid

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from common import helper

compiler = 'javac'
ext = '.java'

@magics_class
class JavaPlugin(Magics):
    
    def __init__(self, shell):
        super(JavaPlugin, self).__init__(shell)
        self.argparser = helper.get_argparser()
    
    @staticmethod
    def compile(file_path, flags):
        args = [compiler, file_path + ext]

        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            args.append(flag)
        
        subprocess.check_output(args, stderr=subprocess.STDOUT)

    def run_java(self, file_path):
        
        output = subprocess.check_output(["java", file_path], stderr=subprocess.STDOUT)
        output = output.decode('utf8')
            
        helper.print_out(output)
    
    def run_version(self):
        args = ['java', '--version']
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)

    @cell_magic
    def java(self, line, cell):
        args = line.split()

        if '-v' in args or '--version' in args:
            self.run_version()
            return

        line = cell.split("\n")

        name_file = "Main"
        for l in line:
            if l:
                if "public class " in l:
                    name_file = l.replace("public class ","").replace("{","").replace(" ","")
                    break

        file_path = name_file
        #print(file_path)
        #print(cell)
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.compile(file_path, args)
            self.run_java(file_path)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))