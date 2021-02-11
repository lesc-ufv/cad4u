from distutils.core import setup

setup(
    name='ColabPlugin',
    version='blind',
    author='blind',
    author_email='blind',
    py_modules=['plugin', 'nvcc.nvcc', 'c.c', 'cpp.cpp', 'verilog.verilog', 'java.java', 'gem5.gem5', 'valgrind.valgrind', 'common.helper'],
    url='https://github.com/blindreviewsrc/blind/',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++, GCC code, Verilog, Gem5',
    # long_description=open('README.md').read(),
)
