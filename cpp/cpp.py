import os
import subprocess
import tempfile
import uuid

from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
from common import helper

compiler = '/usr/bin/g++'
ext = '.cpp'

@magics_class
class CPPPlugin(Magics):
    
    def __init__(self, shell):
        super(CPPPlugin, self).__init__(shell)
        self.argparser = helper.get_argparser()
    
    @staticmethod
    def compile(file_path, flags):
        args = [compiler, file_path + ext, "-o", file_path + ".out"]

        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            if flag == "<":
                break
            args.append(flag)
        
        subprocess.check_output(args, stderr=subprocess.STDOUT)

    def run_gcc(self, file_path):
        args = [file_path + ".out", "< 10"]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
            
        helper.print_out(output)
    
    def run_version(self):
        args = [compiler, '--version']
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)

    @cell_magic
    def cpp(self, line, cell):
        args = line.split()

        if '-v' in args or '--version' in args:
            self.run_version()
            return

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ext, "w") as f:
                f.write(cell)
            try:
                self.compile(file_path, args)
                self.run_gcc(file_path)
            except subprocess.CalledProcessError as e:
                helper.print_out(e.output.decode("utf8"))