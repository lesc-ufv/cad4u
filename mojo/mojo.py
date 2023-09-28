from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

compiler = "/root/.modular/pkg/packages.modular.com_mojo/bin/mojo"

@magics_class
class MOJOPlugin(Magics):
    
    def __init__(self, shell):
        super(MOJOPlugin, self).__init__(shell)
    
    def updateInstall(self):
        list_dependecies = ["mojo"]
        if not self.already_install:
            self.already_install = True
            tool.install(list_dependecies)

    @cell_magic
    def mojo(self, line, cell):
        colab = tool.Colab()
        colab.install_script("mojo/install.sh", "mojo")
        colab.write_file(cell, "code.mojo")
        colab.command_line(f'{compiler} build /content/code.mojo')
        colab.execute("code")