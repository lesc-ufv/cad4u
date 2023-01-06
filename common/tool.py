import subprocess
import argparse

'''
def get_argparser():
    parser = argparse.ArgumentParser(description='Colab params')
    parser.add_argument("-h", "--help", action='store_true',
                        help='flag to return help')
    parser.add_argument("-p", "--params", action='store_true',
                        help='flag to return the parameters')
    return parser
'''

class Colab():

    def __init__(self):
        self.already_install = False
    
    def print_out(self, out: str):
        for l in out.split('\n'):
            print(l)

    def install(self, list, toolName=""):
        if not self.already_install:
            self.already_install = True

            print("Installing %s. Please wait... " % (toolName), end="")
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

        with open(file_path, "w") as f:
            f.write(cell)
        try:
            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode('utf8') 
        except subprocess.CalledProcessError as e:
            self.print_out(e.output.decode("utf8"))
    
    def execute(self, prog, file_path, print_output=True):

        args = [file_path]

        try:
            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode('utf8')
            self.print_out(out)
        except subprocess.CalledProcessError as e:
            self.print_out(e.out.decode("utf8"))