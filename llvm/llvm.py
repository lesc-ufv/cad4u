from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

@magics_class
class llvmPlugin(Magics):
    
    def __init__(self, shell):
        super(llvmPlugin, self).__init__(shell)

    @cell_magic
    def opt(self, line, cell):

        colab = tool.Colab()
        colab.install(["llvm-10", "clang-10"])

        if "--help" in line:
            colab.command_line("opt-10 --help", True)
            line.replace("--help", "")

        line += " -fno-discard-value-names -Xclang -disable-O0-optnone -S -emit-llvm"

        colab.compile("clang-10", cell, "code.cpp", "code.ll", line.split())

        colab.print_cfg("--dot-cfg", "code.ll")