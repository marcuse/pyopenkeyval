#!/usr/bin/env python

from distutils.core import setup
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
    name='pyopenkeyval',
    version='0.4',
    description='pyopenkeyval: A simple interface to OpenKeyval.org',
    long_description='A simple, dict-like interface to read and write values on the OpenKeyval service.',
    author='Marcus Ekelund',
    author_email='marcus.ekelund@gmail.com',
    url='http://github.com/marcuse/pyopenkeyval',
    py_modules=['pyopenkeyval'],
    license="Public domain",
    platforms=["any"],
    cmdclass={'build_py': build_py},
)
