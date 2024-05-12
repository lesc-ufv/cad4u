from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

@magics_class
class Plugin(Magics):
    
    def __init__(self, shell):
        super(Plugin, self).__init__(shell)
    
    @cell_magic
    def gcc(self, line, cell):
        colab = tool.Colab()
        colab.install(["gcc"])
        colab.compile("gcc", cell, "code.c", flags=line.split())
        colab.execute()