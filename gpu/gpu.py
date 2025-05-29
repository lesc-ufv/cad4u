import os
import subprocess
import tempfile
import uuid

from IPython.core.magic import Magics, cell_magic, magics_class
from common import helper

compiler = '/usr/local/cuda/bin/nvcc'
ext = '.cu'
 
@magics_class
class Plugin(Magics):

    def __init__(self, shell):
        super(Plugin, self).__init__(shell)
        self.argparser = helper.get_argparser()

    @staticmethod
    def compile(file_path, flags):

        args = [compiler, file_path + ext, "-o", file_path + ".out"]
        flags.append('-arch=sm_75 -gencode=arch=compute_75,code=sm_75')
        
        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            args.append(flag)
        
        subprocess.check_output(args, stderr=subprocess.STDOUT)
    
    @staticmethod
    def compile_ptx(file_path, flags):
        arch = '50'
        if (len(flags) > 0):
            arch = flags[0]

        #-arch=sm_'+arch
        args = [compiler,'--generate-code', 'arch=compute_'+arch+',code=sm_'+arch, file_path + ext, '--ptx']
        
        subprocess.check_output(args, stderr=subprocess.STDOUT)

    def run(self, file_path):
        output = subprocess.check_output([file_path + ".out"], stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)
    
    def run_nvprof(self, file_path, flags):

        if len(flags) == 0:
            args = ["nvprof", file_path + ".out"]
        else:
            flag = ""
            for f in flags:
                flag += " -m " + f

            args = ["sh", "/content/cad4u/cuda/metric.sh", flag]

        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)
    
    def run_nvprof_all_metrics(self, file_path):
        args = ["nvprof", "--metrics", "all", file_path + ".out"]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)

    def run_ptx(self, file_path):
        args = ["cat", file_path + ".ptx"]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        helper.print_out(output)

    @cell_magic
    def cu(self, line, cell):
        args = line.split()

        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, str(uuid.uuid4()))
            with open(file_path + ext, "w") as f:
                f.write(cell)
            try:
                self.compile(file_path, args)
                self.run(file_path)
            except subprocess.CalledProcessError as e:
                helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def gpu(self, line, cell):
        args = line.split()

        file_path = os.path.join('/content/code')
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.compile(file_path, args)
            self.run(file_path)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def nvprof(self, line='', cell=None):
        args = line.split()

        file_path = os.path.join('/content/code')
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.compile(file_path, [])
            self.run_nvprof(file_path, args)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def nvprof_all(self, line='', cell=None):
        args = line.split()

        file_path = os.path.join('/content/code')
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.compile(file_path, args)
            self.run_nvprof_all_metrics(file_path)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
    
    @cell_magic
    def ptx(self, line='', cell=None):
        args = line.split()

        file_path = os.path.join('/content/code')
        with open(file_path + ext, "w") as f:
            f.write(cell)
        try:
            self.compile_ptx(file_path, args)
            self.run_ptx(file_path)
        except subprocess.CalledProcessError as e:
            helper.print_out(e.output.decode("utf8"))
