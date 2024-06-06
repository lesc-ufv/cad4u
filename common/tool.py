import subprocess, argparse, os, json, sys

from IPython.display import display, Image, SVG, IFrame
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

import matplotlib.pyplot as plt
from ipywidgets import *

already_install = []
already_install_pip = []


class Colab:

    __grid = GridspecLayout(1, 1)
    __grid_values = {}
    __param_values = ""
    __program = ""
    __flag = ""
    __input = ""
    __pos = 0

    def print_out(self, out: str):
        for l in out.split("\n"):
            print(l)

    def print_custom(self, output: str, start: str, end: str) -> None:
        if output == None: 
            return
        is_out = False
        for out in output.split("\n"):
            if end in out:
                is_out = False
            if is_out:
                print(out)
            if start in out:
                is_out = True

    def argument(self, list_args, string, default=None) -> str:
        name = default
        data = string.split(" ")
        for i, l in enumerate(data):
            for la in list_args:
                if la in l:
                    for j in (i + 1, len(data) - 1):
                        if data[j] != "":
                            name = string.split(" ")[i + 1]
                            break
                    break
        return name

    def arguments(
        self,
        args: str,
        line: str,
        text: str = "",
        type: str = str,
        required: bool = False,
        default=None,
    ):
        parser = argparse.ArgumentParser(text)
        parser.add_argument(f"--{args}", type=type, required=required, default=default)
        return parser.parse_args()

    def install(self, list):
        global already_install
        count = 0
        for l in list:
            if l not in already_install:
                already_install.append(l)
                if count == 0:
                    print("Installing. Please wait... ", end="")
                output = subprocess.check_output(
                    ["apt", "update"], stderr=subprocess.STDOUT
                )
                try:
                    output = subprocess.check_output(
                        ["apt", "install", l], stderr=subprocess.STDOUT
                    )
                    output = output.decode("utf8")
                except subprocess.CalledProcessError as e:
                    self.print_out(e.output.decode("utf8"))
                    print("failed!")
                count += 1
        if count > 0:
            print("done!")

    def install_pip(self, list):
        global already_install_pip
        count = 0
        for l in list:
            if l not in already_install_pip:
                already_install_pip.append(l)
                if count == 0:
                    print("Installing pip dependecies. Please wait... ", end="")
                try:
                    output = subprocess.check_output(
                        ["pip3", "install", l], stderr=subprocess.STDOUT
                    )
                    output = output.decode("utf8")
                except subprocess.CalledProcessError as e:
                    self.print_out(e.output.decode("utf8"))
                    print("failed!")
                count += 1
        if count > 0:
            print("done!")

    def install_script(self, path_script, nickname):
        global already_install
        count = 0
        if nickname not in already_install:
            already_install.append(nickname)
            if count == 0:
                print("Installing. Please wait... ", end="")
            output = subprocess.check_output(
                ["apt", "update"], stderr=subprocess.STDOUT
            )
            try:
                self.command_line("sh /content/cad4u/" + path_script)
                output = output.decode("utf8")
            except subprocess.CalledProcessError as e:
                self.print_out(e.output.decode("utf8"))
                print("failed!")
            count += 1
        if count > 0:
            print("done!")

    def write_file(self, cell, file_path):
        with open("/content/" + file_path, "w") as f:
            f.write(cell)

    def compile(
        self,
        compiler,
        cell,
        file_path,
        file_output="code.out",
        flags=[],
        no_output=False,
    ):

        if no_output:
            args = [compiler, file_path]
        else:
            args = [compiler, file_path, "-o", file_output]

        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            if flag == "<":
                break
            args.append(flag)

        try:
            if "-v" in flags or "--version" in flags:
                self.run_version(compiler)

            with open("/content/" + file_path, "w") as f:
                f.write(cell)

            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode("utf8")
        except subprocess.CalledProcessError as e:
            print("The process occurred error, see below the error:\n")
            self.print_out(e.output.decode("utf8"))

    def run_version(self, compiler):
        self.command_line("%s --version" % (compiler), True)

    def execute(self, file_path="code.out", print_output=True):
        try:
            args = ["/content/" + file_path]
            output = subprocess.check_output(args, stderr=subprocess.STDOUT).decode(
                "utf8"
            )
            self.print_out(output)
        except subprocess.CalledProcessError as e:
            self.print_out(e.output.decode("utf8"))

    def command_line(self, command, print_output=False):
        try:
            output = subprocess.check_output(
                command.split(" "), stderr=subprocess.STDOUT
            ).decode("utf8")
            if print_output:
                self.print_out(output)
            return output
        except subprocess.CalledProcessError as e:
            self.print_out(e.output.decode("utf8"))

    def print_cfg(self, optimization, input_path):
        self.command_line(
            "sh /content/cad4u/llvm/execute.sh "
            + optimization
            + " /content/"
            + input_path
        )
        for file in os.listdir("/content"):
            if file.endswith(".dot"):
                name = "/content/" + file
                self.command_line("dot -Tpng " + name + " -o " + name + ".png")
                self.display_png(name + ".png")

    def display_png(self, file_path):
        if ".png" not in file_path:
            file_path += ".png"
        display(filename=file_path)

    def display_svg(self, file_path):
        if ".svg" not in file_path:
            file_path += ".svg"
        display(SVG("/content/" + file_path))

    def display_wavedrowm(self, file_path):

        from vcd2wavedrom import vcd2wavedrom

        vcd2wavedrom.main(
            [
                "-i",
                "/content/" + file_path + ".vcd",
                "-o",
                "/content/" + file_path + ".json",
            ]
        )

        import wavedrom

        f = open(file_path + ".json", "r")
        s = ""
        for l in f.readlines():
            s += l.strip()
        f.close()

        svg = wavedrom.render("""%s""" % (s))
        svg.saveas("/content/output.svg")
        self.display_svg("output.svg")

    def show(self):
        display(self.__grid)

    def grid(self, number_row, number_col=10):
        self.__grid = GridspecLayout(number_row, 10)

    def text(self, desc):
        self.__grid[self.__pos, 0] = Button(
            description=desc,
            button_style="warning",
            layout=Layout(height="auto", width="auto"),
        )
        self.__pos += 1

    def on_value_change(self, change):
        self.__grid_values[change["owner"].name] = int(
            change["owner"].options[change["owner"].index]
        )

    def dropdown(self, id, description, opt_list):
        self.__grid[self.__pos, 0] = Button(
            description=description,
            button_style="warning",
            layout=Layout(height="auto", width="auto"),
        )
        dropdown = Dropdown(
            description="",
            layout=Layout(height="30px", width="auto"),
            value=opt_list[0],
            options=opt_list,
        )
        dropdown.name = id
        self.__grid_values[id] = dropdown.value
        dropdown.observe(self.on_value_change, names="value")
        self.__grid[self.__pos, 1] = dropdown
        self.__pos += 1

    def parse_out_valgrind(self, out, print_file=False):
        c = 0
        print(
            "Parameters: %d, %d, %d\n"
            % (
                1024 * self.__grid_values["size"],
                self.__grid_values["assoc"],
                self.__grid_values["lines"],
            )
        )
        if print_file:
            f = open("/content/print_out.txt", "w")
        for l in out.split("\n"):
            if c > 12:
                res = l.split("==")
                if len(res) > 1:
                    print(res[2][1:])
                    if print_file:
                        f.write(res[2][1:] + "\n")
            c += 1

    def on_button_clicked(self, b):
        if b.name == "__exec__":
            b.button_style = "danger"
            b.description = "wait"

            self.parameter(self.__flag)

            print("--" * 30)
            if self.__program == "valgrind":
                out = self.command_line(
                    "%s --tool=cachegrind %s /content/%s"
                    % (self.__program, self.__param_values, self.__input),
                    False,
                )
                self.parse_out_valgrind(out)
            else:
                self.command_line(
                    "%s %s /content/%s &> "
                    % (self.__program, self.__param_values, self.__input),
                    True,
                )

            print("--" * 30)
            b.button_style = "success"
            b.description = "Start execution"

    def exec(self, program, input, flag):
        self.__program = program
        self.__input = input
        self.__flag = flag
        btn = Button(
            description="Start execution",
            button_style="success",
            layout=Layout(height="auto", width="auto"),
        )
        btn.name = "__exec__"
        btn.on_click(self.on_button_clicked)
        self.__grid[self.__pos, 0] = btn
        self.__pos += 1

    def parameter(self, p):
        s = p
        s += str(1024 * (self.__grid_values["size"]))
        s += "," + str(self.__grid_values["assoc"])
        s += "," + str(self.__grid_values["lines"])
        self.__param_values = s

    def bash_script(self, name_file: str, info: str, append=True):
        """
        create a bash script from the scratch
        """
        f = open(name_file, "a" if append else "w")
        f.write(info + "\n")
        f.close()
