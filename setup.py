import sys
import os
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

#####################################
VERSION = "1.0.{build}"
ISRELEASED = False
__version__ = VERSION
#####################################

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

if os.environ['CONDA_BUILD']:
    with open('__conda_version__.txt', 'w') as f:
        if ISRELEASED:
            f.write(VERSION)
        else:
            f.write(VERSION + '.dev')

extension_module = Extension(
    'pagral.graph.graph_data',
    sources=["./pagral/graph/graph_data.pyx"]
)

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

    ext_modules=cythonize([extension_module]),
    zip_safe=False,
    license='GPL3',
    # entry_points={
    #     'console_scripts': [
    #         'pyntacle = pyntacle.pyntacle:App'
    #     ]
    # },
    # setup_requires=['numpy'],
    install_requires=[
        "numpy",
        "cython",
        "sphinx",
    ],
)
