from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

@magics_class
class Plugin(Magics):
    
    def __init__(self, shell):
        super(Plugin, self).__init__(shell)

    @cell_magic
    def rust(self, line, cell):
        colab = tool.Colab()
        colab.install(["rustc"])
        colab.compile("rustc", cell, "code.rs", "code.out", line.split())
        colab.execute("code.out")
       
    