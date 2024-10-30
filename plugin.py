from cad4u.gpu.gpu import Plugin as GPU
from cad4u.c.c import Plugin as C
from cad4u.cpp.cpp import Plugin as CPP
from cad4u.hdl.hdl import Plugin as HDL
from cad4u.java.java import Plugin as JAVA
from cad4u.gem5.gem5 import Plugin as GEM5
from cad4u.valgrind.valgrind import Plugin as VALGRIND
from cad4u.llvm.llvm import Plugin as LLVM
from cad4u.rust.rust import Plugin as RUST
from cad4u.mojo.mojo import Plugin as MOJO


def load_ipython_extension(ip):
	ip.register_magics(GPU(ip))
	ip.register_magics(C(ip))
	ip.register_magics(CPP(ip))
	ip.register_magics(HDL(ip))
	ip.register_magics(JAVA(ip))
	ip.register_magics(GEM5(ip))
	ip.register_magics(VALGRIND(ip))
	ip.register_magics(LLVM(ip))
	ip.register_magics(RUST(ip))
	ip.register_magics(MOJO(ip))
