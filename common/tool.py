import subprocess
import argparse

from IPython.display import display, Image, SVG
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring

import matplotlib.pyplot as plt 
from ipywidgets import *

already_install = False

class Colab():

    def __init__(self):
        grid = GridspecLayout(1, 1)
        values_grid = {}
    
    def print_out(self, out: str):
        for l in out.split('\n'):
            print(l)

    def install(self, list):
        global already_install
        if not already_install:
            already_install = True
            print("Installing. Please wait... ", end="")
            output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT) 
            try:
                output = subprocess.check_output(["apt", "install"] + list, stderr=subprocess.STDOUT) 
                output = output.decode('utf8')
                print("done!")
            except subprocess.CalledProcessError as e:
                self.print_out(e.output.decode("utf8"))
                print("failed!")
    
    def compile(self, compiler, cell, file_path, file_output, flags):

        args = [compiler, file_path, "-o", file_output]

        # adding flags: -O3, -unroll-loops, ...
        for flag in flags:
            if flag == "<":
                break
            args.append(flag)

        with open("/content/"+file_path, "w") as f:
            f.write(cell)
        try:
            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode('utf8') 
        except subprocess.CalledProcessError as e:
            self.print_out(e.output.decode("utf8"))
    
    def execute(self, file_path, print_output=True):

        args = ["/content/"+file_path]

        try:
            out = subprocess.check_output(args, stderr=subprocess.STDOUT)
            out = out.decode('utf8')
            self.print_out(out)
        except subprocess.CalledProcessError as e:
            self.print_out(e.out.decode("utf8"))
    
    def command_line(self, command, print_output=False):
        try:
            out = subprocess.check_output(command.split(" "), stderr=subprocess.STDOUT).decode('utf8')
            if (print_output):
                self.print_out(out)
            return out
        except subprocess.CalledProcessError as e:
            self.print_out(e.out.decode("utf8"))

    def print_cfg(self, command):
        out = self.command_line(command)
        print(out)
        for l in out.split("\n"):
            if "Writing" in l:
                name = l.split(" ")[1].replace("'","").replace("...","")
                self.command_line("dot -Tpng "+name+" -o /content/"+name+".png")
                self.display_png("/content/"+name+".png")
                
    def display_png(self, file_path):
        if ".png" not in file_path:
            file_path += ".png"
        display(filename="/content"+file_path)

    def display_svg(self, file_path):
        if ".svg" not in file_path:
            file_path += ".svg" 
        display(SVG('/content/'+file_path))
    
    def show(self):
        display(self.grid)
    
    def grid(self, x, y):
        self.grid = GridspecLayout(x, y)
    
    def text(self, desc, x, y):
        self.grid[x,y] = Button(description=desc, button_style="warning", layout=Layout(height='auto', width='auto'))

    def on_value_change(self, change):
        self.values_grid[change['owner'].name] = int(change['owner'].options[change['owner'].index])
        print(self.values_grid)

    def dropdown(self, id, desc, opt_list, increment, x, y):
        dropdown = Dropdown(description=desc, layout=Layout(height='30px', width='auto'), value=increment, options=opt_list)
        dropdown.name = id
        dropdown.observe(self.on_value_change, names='value')
        self.grid[x,y] = dropdown
    

'''
    botao(ID,descricao,i,j) - botao com o texto descricao, o ID que será gravado 
    em um dicionario para recuperar o IDX de onde esta seu valor na lista

    dropdown(ID,descricao,lista_opcoes)

    texto(ID,descricao)

    slider(ID,descricao)

    os botoes escrevem o valor no dicionario
    valor(ID)

    para criar 3 botoes
    grid(3,1)
    dropdown("linha","Tamanho da Linha Cache",[2,4,8,16],0,0)
    dropdown("assoc","Associativadade Cache",[1,2,4,8],1,0)
    dropdown("Tamanho","Tamanho Cache KB",[1,2,4,8,16,32,64],2,0)
'''