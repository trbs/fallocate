#!/usr/bin/env python

import os
import sys
import glob
from distutils.command.build_ext import build_ext
from distutils.core import setup
from distutils.extension import Extension

__version__ = "1.0"

def find_in_file(filename, s):
    try:
        for line in open(filename):
            if s in line:
                return True
    except IOError:
        return False

def find_in_glob(g, s):
    for filename in glob.glob(g):
        if find_in_file(filename, s):
            return True
    return False

defs = []

if sys.platform == "darwin":
    if find_in_file("/usr/include/sys/fcntl.h", "F_ALLOCATECONTIG"):
        defs.append(("HAVE_APPLE_F_ALLOCATECONTIG", None))
else:
    if find_in_glob("/usr/include/*/bits/fcntl.h", "fallocate"):
        defs.append(("HAVE_FALLOCATE", None))
    if find_in_file("/usr/include/fcntl.h", "posix_fallocate"):
        defs.append(("HAVE_POSIX_FALLOCATE", None))
    if find_in_file("/usr/include/fcntl.h", "posix_fadvise"):
        defs.append(("HAVE_POSIX_FADVISE", None))


_fallocate = Extension('fallocate/_fallocate', sources=['fallocate/_fallocatemodule.c'], define_macros=defs)

setup(
    name = "fallocate",
    version = __version__,
    description = "Module to expose posix_fallocate(3), posix_fadvise(3) and fallocate(2)",
    long_description = """
=========
fallocate
=========

fallocate exposes an interface to fallocate(2), posix_fallocate(3) and posix_fadvise(3).

Under Mac OS X the fallocate() method will use the apple equivalent of fallocate(2).
Note that this might not be exactly the same.

When using the wrapper functions around the fallocate(2) call, this is the default, the
arguments given to the function are slightly different then the c call.

This module has the arguments like:

::

  fallocate(fd, offset, length, mode=0)

While in C the function looks like:

::

  fallocate(fd, mode, offset, length)

The main reason for this is that the mode argument tends not to be used much and thus
having the default as a keyword argument is much easier then having to specify 0 everytime.
    """,
    author = "I.S. van Oostveen",
    author_email = "trbs@trbs.net",
    url = "https://github.com/trbs/fallocate",
    license = "Python License",
    keywords = "posix_fallocate posix_fadvise fallocate",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
    packages = [
        'fallocate',
    ],
    ext_modules = [_fallocate],
    cmdclass = {
        'build_ext': build_ext,
    },
)

