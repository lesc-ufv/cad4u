from distutils.core import setup

setup(
    name='ColabPlugin',
    version='1.0',
    author='Michael Canesche',
    author_email='michael.canesche@gmail.com',
    py_modules=['plugin', 'cuda.cuda', 'c.c', 'cpp.cpp', 'verilog.verilog', 'java.java', 'gem5.gem5', 'valgrind.valgrind', 'common.helper'],
    url='https://github.com/lesc-ufv/cad4u',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA, C/C++, GCC code, Verilog, Gem5',
    # long_description=open('README.md').read(),
)
