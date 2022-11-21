# setup file for CPython package

from setuptools import setup, Extension

module1 = Extension(
    'demo',
    sources = ['demo.c'],
)

setup(
    name = 'PackageName',
    version='1.0',
    description='This is a demo package',
    ext_modules = [module1]
)