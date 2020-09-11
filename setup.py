import os
import re
import sys
import numpy
from setuptools import setup, find_packages, Extension


try:
    from importlib import util
except ImportError:
    sys.stdout.write(
        "\nIt seems that importlib library is not available on this machine. Please install pip (e.g. for Ubuntu, "
        "run 'sudo apt-get install python3-pip'.\n")
    sys.exit()

if util.find_spec("setuptools") is None:
    sys.stdout.write(
        "\nIt seems that setuptools is not available on this machine. Please install pip (e.g. for Ubuntu, run 'sudo "
        "apt-get install python3-pip'.\n")
    sys.exit()

if sys.version_info <= (3, 7):
    sys.exit('Sorry, Python < 3.7 is not supported.')

try:
    from Cython.Distutils import build_ext
except ImportError:
    USE_CYTHON = False
else:
    USE_CYTHON = True
ext = '.pyx' if USE_CYTHON else '.cpp'

extension_module = Extension(
    'pagral.graph.adjacency_matrix',
    sources=["./pagral/graph/adjacency_matrix" + ext],
    include_dirs=[numpy.get_include()],
    define_macros=[("NPY_NO_DEPRECATED_API",)],
)

if USE_CYTHON:
    from Cython.Build import cythonize

    extension_module = cythonize([extension_module],
                                 compiler_directives={'language_level': "3"},
                                 annotate=True)


# if sys.argv[1] == "install":
#     print(sys.argv)
#     del sys.argv[4]

VERSION = os.environ['APPVEYOR_BUILD_VERSION']

print(VERSION)
print(os.environ['PKG_VERSION'])

print("version {} passed to setup.py".format(VERSION))
assert re.match('^[0-9]+\.[0-9]+\.[0-9]+$', VERSION), "Invalid version number"

setup(
    name='pagral',
    version=VERSION,
    author='Tommaso Mazza',
    author_email='t.mazza@css-mendel.it',
    description='Pagral: a PArallel python GRAph Library',
    long_description=open('./conda-recipe/README.txt').read(),

    packages=find_packages(),
    include_package_data=True,

    ext_modules=extension_module,
    zip_safe=False,
    license='GPL3',
    install_requires=[
        "numpy==1.19.1",
        "cython",
    ],
)
