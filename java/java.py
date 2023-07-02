from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

@magics_class
class JavaPlugin(Magics):
    
    def __init__(self, shell):
        super(JavaPlugin, self).__init__(shell)

    @cell_magic
    def java(self, line, cell):

        name_file = "Main"
        for l in cell.split("\n"):
            if l and "public class " in l:
                name_file = l.replace("public class ","").replace("{","").replace(" ","")
                break

        colab = tool.Colab()
        colab.compile("javac", cell, name_file+".java", flags=line.split(), no_output=True)
        colab.command_line("java "+name_file, print_output=True)