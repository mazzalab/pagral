import sys
from setuptools import setup, find_packages, Extension

import numpy

########################
VERSION = "0.1"
ISRELEASED = False
__version__ = VERSION
########################

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
    'pagral.graph.graph_data',
    sources=["./pagral/graph/graph_data"+ext],
    include_dirs=[numpy.get_include()],
    define_macros=[("NPY_NO_DEPRECATED_API",)],
)

if USE_CYTHON:
    from Cython.Build import cythonize
    extension_module = cythonize([extension_module],
                                 compiler_directives={'language_level': "3"},
                                 annotate=True)

setup(
    name='pagral',
    version=VERSION,
    author='Tommaso Mazza',
    author_email='t.mazza@css-mendel.it',
    description='Pagral: a PArallel python GRAph Library',
    long_description=open('./conda-recipe/README.txt').read(),

    packages=find_packages(),
    # packages=['pyappveyordemo', 'pyappveyordemo.tests'],
    include_package_data=True,

    ext_modules=extension_module,
    zip_safe=False,
    license='GPL3',
    # entry_points={
    #     'console_scripts': [
    #         'pyntacle = pyntacle.pyntacle:App'
    #     ]
    # },
    # setup_requires=['numpy'],
    install_requires=[
        "numpy==1.19.1",
        "cython",
    ],
)
