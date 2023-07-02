from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool

from IPython.display import display, HTML

@magics_class
class VERILOGPlugin(Magics):
    
    def __init__(self, shell):
        super(VERILOGPlugin, self).__init__(shell)

    @cell_magic
    def verilog(self, line, cell):
        colab = tool.Colab()
        colab.install(["iverilog", "python3-cairosvg", "yosys"])
        colab.compile("iverilog", cell, "code.v", "code.out", line.split())
        colab.execute("code.out")
       
    @cell_magic
    def print_verilog(self, line, cell):
        
        colab = tool.Colab()
        colab.install(["iverilog", "python3-cairosvg", "yosys"])

        if "-top" not in line: 
            args = "yosys -Q -T -q -s /content/cad4u/verilog/script.ys"
        else:
            args = '/content/cad4u/verilog/yosys_command.sh ' + line.replace("-top","").replace(" ","") + ' code.v'
            print(args)
        
        colab.compile("iverilog", cell, "code.v", "code.out")
        colab.command_line(args)
        colab.command_line('/content/cad4u/verilog/netlistsvg/bin/netlistsvg.js output.json --skin /content/cad4u/verilog/netlistsvg/lib/default.svg')
        colab.display_svg('out.svg')
        
    @cell_magic
    def waveform(self, line, cell):

        colab = tool.Colab()
        colab.install(["iverilog", "python3-cairosvg", "yosys"])

        args = line.split()

        if len(args) > 0:
            name = args[0]
            if '.vcd' not in name:
                name += '.vcd'
        else:
            print("Name of file not exist! Please give the name.")
            print("Ex. \%\%waveform <name_file>.vcd")
            exit(0)
        
        import sys
        sys.path.insert(0,'.')
        from cad4u.verilog.vcd_parser.vcd_plotter import VcdPlotter

        op_dict = []
        sign_list = []
        time_begin = []
        time_end = []
        base = []
        flag_op_dict = False

        for l in cell.strip().split("\n"):
            l = l.split("#")[0]
            if l == '':
                continue
            if 'sign_list' not in l and 'op_dict' not in l:
                s = l.replace('=', '+=[') + ']'
                exec(s)
            else:
                if 'op_dict' in l:
                    flag_op_dict = True
                exec(l.replace('=', '+='))
        if flag_op_dict == False:
            op_dict = [[{}]]
            
        vcd_plt = VcdPlotter('/content/%s'%name)
        vcd_plt.show(op_dict, sign_list, time_begin[0], time_end[0], base[0])

    @cell_magic
    def wavedrom(self, line, cell):
        
        colab = tool.Colab()

        colab.install(["iverilog", "python3-cairosvg", "yosys"])
        colab.install_pip(["vcdvcd", "git+https://github.com/Toroid-io/vcd2wavedrom.git", "wavedrom"])
        colab.compile("iverilog", cell, "code.v", "code.out", line.split())
        colab.execute("code.out")

        from vcd2wavedrom import vcd2wavedrom 
        vcd2wavedrom.main(['-i', '/content/dump.vcd', '-o', '/content/dump.json'])

        colab.display_wavedrowm('/content/dump.json')
        
        