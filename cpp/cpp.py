from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

@magics_class
class CPPPlugin(Magics):
    
    def __init__(self, shell):
        super(CPPPlugin, self).__init__(shell)
    
    @cell_magic
    def cpp(self, line, cell):
        colab = tool.Colab()
        colab.install(["g++"])
        colab.compile("g++", cell, "code.cpp", flags=line.split())
        colab.execute()