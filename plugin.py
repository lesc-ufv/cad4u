from gpu.gpu import GPUPlugin as GPU
from c.c import CPlugin as C
from cpp.cpp import CPPPlugin as CPP
from java.java import JavaPlugin as JAVA
from hdl.hdl import HDLPlugin as HDL
from valgrind.valgrind import ValgrindPlugin as VALGRIND
from gem5.gem5 import Gem5Plugin as GEM5
from llvm.llvm import llvmPlugin as LLVM
from rust.rust import RUSTPlugin as RUST
from mojo.mojo import MOJOPlugin as MOJO


def register_plugin(ip, tool):
    ip.register_magics(tool(ip))


def load_ipython_extension(ip):
    class_list = [GPU, C, CPP, JAVA, HDL, VALGRIND, GEM5, LLVM, RUST, MOJO]
    for tool in class_list:
        register_plugin(ip, tool)
