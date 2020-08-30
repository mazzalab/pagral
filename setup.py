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

if '--use-cython' in sys.argv:
    USE_CYTHON=True
    sys.argv.remove('--use-cython')
else:
    USE_CYTHON = False
ext = '.pyx' if USE_CYTHON else '.c++'

extension_module = Extension(
    'pagral.graph.graph_data',
    sources=["./pagral/graph/graph_data"+ext],
    include_dirs=[numpy.get_include()],
    language='c++',
    define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
)

if USE_CYTHON:
    from Cython.Build import cythonize
    extension_module = cythonize(extension_module)


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

    ext_modules=[extension_module],
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
