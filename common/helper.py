import argparse
import subprocess

def get_argparser():
    parser = argparse.ArgumentParser(description='NVCCPlugin params')
    parser.add_argument("-t", "--timeit", action='store_true',
                        help='flag to return timeit result instead of stdout')
    return parser


def print_out(out: str):
    for l in out.split('\n'):
        print(l)


def updateInstall(args, toolName=""):
    print("Installing %s. Please wait... " % (toolName), end="")
    subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT)
    try:
        output = subprocess.check_output(args.split(" "), stderr=subprocess.STDOUT)
        output = output.decode('utf8')
        print("done!")
    except subprocess.CalledProcessError as e:
        print_out(e.output.decode("utf8"))
        print("failed!")
