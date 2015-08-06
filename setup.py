from distutils.core import setup
from numpy.distutils.misc_util import get_numpy_include_dirs
from distutils.extension import Extension
import os

# you can customize
os.environ["CC"] = "clang"
os.environ["CXX"] = "clang"

convolve = Extension("convolve",
                    include_dirs = get_numpy_include_dirs(),
                    sources = ["convolve.c"])
setup(
    name = "PyCyExamp",
    version = '1.0',
    packages = ['pycyexamp'],
    package_dir = {'pycyexamp': ''},
    ext_package = 'pycyexamp',
    ext_modules = [convolve]
)
