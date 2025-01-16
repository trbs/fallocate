#!/usr/bin/env python

import sys
import glob
import warnings
from distutils.command.build_ext import build_ext
from distutils.core import setup
from distutils.extension import Extension
from fallocate import __version__


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


def with_prefix(prefixen, func):
    def newfunc(*args):
        for prefix in prefixen:
            if func(prefix + args[0], *args[1:]):
                return True
        return False
    return newfunc


defs = []

if sys.platform == "darwin":
    XCODE_PREFIX = "/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk"
    find_in_darwin_file = with_prefix(['', XCODE_PREFIX], find_in_file)
    if find_in_darwin_file("/usr/include/sys/fcntl.h", "F_ALLOCATECONTIG"):
        defs.append(("HAVE_APPLE_F_ALLOCATECONTIG", None))
    else:
        warnings.warn(
            "We can't find F_ALLOCATECONTIG on a Mac! This is impossible!")
else:
    if find_in_glob(
            "/usr/include/*/bits/fcntl*.h", "fallocate") or find_in_glob(
                "/usr/include/bits/fcntl*.h", "fallocate"):
        defs.append(("HAVE_FALLOCATE", None))
    if find_in_file("/usr/include/fcntl.h", "posix_fallocate"):
        defs.append(("HAVE_POSIX_FALLOCATE", None))
    if find_in_file("/usr/include/fcntl.h", "posix_fadvise"):
        defs.append(("HAVE_POSIX_FADVISE", None))

if not any(x for x in defs if 'ALLOCATE' in x[0]):
    warnings.warn(
        "Setup.py cannot find a fallocate() or equivalent on your platform ({0}).".
        format(sys.platform))

_fallocate = Extension(
    'fallocate/_fallocate',
    sources=['fallocate/_fallocatemodule.c'],
    define_macros=defs)

setup(
    name="fallocate",
    version=__version__,
    description="Module to expose posix_fallocate(3), posix_fadvise(3) and fallocate(2)",
    long_description=open("README.rst", "r").read(),
    author="I.S. van Oostveen",
    author_email="trbs@trbs.net",
    url="https://github.com/trbs/fallocate",
    license="Python Software Foundation License",
    keywords="posix_fallocate posix_fadvise fallocate",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: Python Software Foundation License',
    ],
    packages=[
        'fallocate',
    ],
    ext_modules=[_fallocate],
    cmdclass={
        'build_ext': build_ext,
    },
)
