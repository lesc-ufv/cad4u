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

def print_out(out: str):
    for l in out.split('\n'):
        print(l)

def updateInstall(list, toolName=""):
    print("Installing %s. Please wait... " % (toolName), end="")
    output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT) 
    try:
        output = subprocess.check_output(["apt", "install"] + list, stderr=subprocess.STDOUT) 
        output = output.decode('utf8')
        print("done!")
    except subprocess.CalledProcessError as e:
        print_out(e.output.decode("utf8"))
        print("failed!")


