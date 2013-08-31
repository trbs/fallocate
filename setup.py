#!/usr/bin/env python

from distutils.command.build_ext import build_ext
from distutils.core import setup
from distutils.extension import Extension

__version__ = "1.0"

_fallocate = Extension('backports/fallocate/_fallocate', sources=['backports/fallocate/_fallocatemodule.c'])

setup(
    name = "backports.fallocate",
    version = __version__,
    description = "Backport of posix_fallocate(3), posix_fadvise(3) and fallocate(2) to Python 2.x",
    author = "I.S. van Oostveen",
    author_email = "trbs@trbs.net",
    url = "https://github.com/trbs/backports.fallocate",
    license = "Python License",
    keywords = "posix_fallocate posix_fadvise fallocate",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
    packages = [
        'backports',
        'backports.fallocate',
    ],
    ext_modules = [_fallocate],
    cmdclass = {
        'build_ext': build_ext,
    },
)

