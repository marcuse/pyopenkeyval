#!/usr/bin/env python

import os
import subprocess
from distutils.core import setup
try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

def md2rst(md_file, fallback):
    pkg_dir = os.path.dirname(__file__)
    rst_conv = ["pandoc", "-f", "markdown", "-t", "rst", os.path.join(pkg_dir, md_file)]
    try:
        return subprocess.check_output(rst_conv)
    except (OSError, subprocess.CalledProcessError):
        return fallback

setup(
    name='pyopenkeyval',
    version='0.4',
    description='pyopenkeyval: A simple interface to OpenKeyval.org',
    long_description=md2rst('README.md', 'A simple, dict-like interface to read and write values on the OpenKeyval service.'),
    author='Marcus Ekelund',
    author_email='marcus.ekelund@gmail.com',
    url='http://github.com/marcuse/pyopenkeyval',
    py_modules=['pyopenkeyval'],
    license="Public domain",
    platforms=["any"],
    cmdclass={'build_py': build_py},
)
