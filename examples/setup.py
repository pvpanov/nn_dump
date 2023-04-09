from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [Extension("cython_example", ["cython_example.pyx"])]

setup(
    ext_modules=cythonize(extensions),
)
