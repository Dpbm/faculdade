from setuptools import setup
from Cython.Build import cythonize

setup(
        name="enada",
        ext_modules=cythonize("test2.pyx")
)
