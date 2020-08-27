from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy

ext_modules = [Extension('graph_data', ['graph_data.pyx'], include_dirs=[numpy.get_include()])]

setup(
    name='Test compilation',
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(ext_modules, compiler_directives={'language_level': "3"}, annotate=True),
    # include_dirs=[numpy.get_include()],
)
