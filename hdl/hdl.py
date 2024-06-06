from IPython.core.magic import Magics, cell_magic, magics_class
from common import tool


@magics_class
class Plugin(Magics):

    def __init__(self, shell):
        super(Plugin, self).__init__(shell)

    @cell_magic
    def verilog(self, line, cell):
        colab = tool.Colab()
        colab.install(["iverilog", "python3-cairosvg", "yosys"])
        name = colab.argument(["-n", "--name"], line, default="code.v")
        colab.compile("iverilog", cell, "code.v", "code.out")
        colab.execute("code.out")
        if name != "code.v":
            colab.command_line("mv /content/code.v " + "/content/" + name)

    @cell_magic
    def vhdl(self, line, cell):
        colab = tool.Colab()
        colab.install(["ghdl", "python3-cairosvg", "yosys"])

        entity = None
        for l in cell.split("\n"):
            if "entity" in l and "is" in l:
                entity = l.strip().split("entity")[1].split("is")[0].replace(" ", "")
                break

        if entity == None:
            print("Not found entity")
            return

        with open("/content/code.vhdl", "w") as f:
            f.write(cell)
        colab.command_line("ghdl -a /content/code.vhdl")
        colab.command_line(f"ghdl -e {entity}")
        colab.command_line(f"ghdl -r {entity}", print_output=True)

    @cell_magic
    def print_verilog(self, line, cell):

        colab = tool.Colab()
        colab.install(["iverilog", "python3-cairosvg", "yosys"])
        name = colab.argument(["-n", "--name"], line, default="code.v")
        top = colab.argument(["-t", "-top"], line, default=None)

        if top:
            args = "/content/cad4u/hdl/yosys_command.sh " + top + " code.v"
        else:
            args = "yosys -Q -T -q -s /content/cad4u/hdl/script.ys"

        colab.compile("iverilog", cell, "code.v", "code.out")
        colab.command_line(args)
        colab.command_line(
            "/content/cad4u/hdl/netlistsvg/bin/netlistsvg.js output.json --skin /content/cad4u/hdl/netlistsvg/lib/default.svg"
        )
        colab.display_svg("out.svg")
        if name != "code.v":
            colab.command_line(f"mv /content/code.v /content/{name}")

    @cell_magic
    def waveform(self, line, cell):

        colab = tool.Colab()
        colab.install(["iverilog", "python3-cairosvg", "yosys"])

        args = line.split()

        if len(args) > 0:
            name = args[0]
            if ".vcd" not in name:
                name += ".vcd"
        else:
            print("Name of file not exist! Please give the name.")
            print("Ex. \%\%waveform <name_file>.vcd")
            exit(0)

        import sys

        sys.path.insert(0, ".")
        from cad4u.hdl.vcd_parser.vcd_plotter import VcdPlotter

        op_dict = []
        sign_list = []
        time_begin = []
        time_end = []
        base = []
        flag_op_dict = False

        for l in cell.strip().split("\n"):
            l = l.split("#")[0]
            if l == "":
                continue
            if "sign_list" not in l and "op_dict" not in l:
                s = l.replace("=", "+=[") + "]"
                exec(s)
            else:
                if "op_dict" in l:
                    flag_op_dict = True
                exec(l.replace("=", "+="))
        if flag_op_dict == False:
            op_dict = [[{}]]

        vcd_plt = VcdPlotter("/content/%s" % name)
        vcd_plt.show(op_dict, sign_list, time_begin[0], time_end[0], base[0])

    @cell_magic
    def wavedrom(self, line, cell):

        colab = tool.Colab()

        colab.install(["iverilog", "python3-cairosvg", "yosys"])
        colab.install_pip(
            ["vcdvcd", "git+https://github.com/Toroid-io/vcd2wavedrom.git", "wavedrom"]
        )
        colab.compile("iverilog", cell, "code.v", "code.out", line.split())
        colab.execute("code.out")
        colab.display_wavedrowm("dump")
    
    @cell_magic
    def systemverilog(self, line, cell):
        colab = tool.Colab()
        colab.install(["python3-cairosvg", "yosys"])
        colab.write_file(cell, "top.sv")
        
        colab.bash_script(f"run_sv.sh", 'yosys -p "read_verilog -sv /content/top.sv; prep -flatten; write_json output.json"', False)
        output = colab.command_line("bash run_sv.sh")

        if "--print" in line:
            colab.command_line(
            "/content/cad4u/hdl/netlistsvg/bin/netlistsvg.js output.json --skin /content/cad4u/hdl/netlistsvg/lib/default.svg"
            )
            colab.display_svg("out.svg")
        if "--stats" in line:
            is_out = False
            for out in output.split("\n"):
                if "CHECK pass" in out:
                    is_out = False
                if is_out:
                    print(out)
                if "Printing statistics" in out:
                    is_out = True

        for out in output.split():
            print(out)
