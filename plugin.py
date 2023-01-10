from cuda.cuda import CudaPlugin as CUDA
from c.c import CPlugin as C
from cpp.cpp import CPPPlugin as CPP
from java.java import JavaPlugin as JAVA
from verilog.verilog import VERILOGPlugin as VERILOG
from valgrind.valgrind import ValgrindPlugin as Valgrind
from gem5.gem5 import Gem5Plugin as GEM5
from llvm.llvm import llvmPlugin as LLVM
from rust.rust import RUSTPlugin as Rust


def load_ipython_extension(ip):
    cuda_plugin = CUDA(ip)
    ip.register_magics(cuda_plugin)

    c_plugin = C(ip)
    ip.register_magics(c_plugin)

    cpp_plugin = CPP(ip)
    ip.register_magics(cpp_plugin)

    verilog_plugin = VERILOG(ip)
    ip.register_magics(verilog_plugin)

    java_plugin = JAVA(ip)
    ip.register_magics(java_plugin)

    ValgrindPlugin = Valgrind(ip)
    ip.register_magics(ValgrindPlugin)

    gem5_plugin = GEM5(ip)
    ip.register_magics(gem5_plugin)

    llvm_plugin = LLVM(ip)
    ip.register_magics(llvm_plugin)

    rust_plugin = Rust(ip)
    ip.register_magics(rust_plugin)
