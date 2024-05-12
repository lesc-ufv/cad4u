from common.generator_plugin import plugin
from distutils.core import setup

class_list = [
    "gpu",
    "c",
    "cpp",
    "hdl",
    "java",
    "gem5",
    "valgrind",
    "llvm",
    "rust",
    "mojo",
]
plugin(class_list)

py_modules = []
for tool in class_list:
    py_modules.append(f"{tool}.{tool}")

setup(
    name="ColabPlugin",
    version="1.0",
    author="Michael Canesche",
    author_email="michael.canesche@gmail.com",
    py_modules=["plugin", "common.helper", "common.tool"] + py_modules,
    url="https://github.com/lesc-ufv/cad4u",
    license="LICENSE",
    description="Jupyter notebook plugin to run CUDA, C/C++, GCC code, Verilog, LLVM, Gem5, Mojo",
    # long_description=open('README.md').read(),
)
