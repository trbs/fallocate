import warnings

__version__ = "1.0.2"

try:
    from ._fallocate import fallocate as _fallocate
    def fallocate(fd, offset, len, mode=0):
        if isinstance(fd, file):
            fd = fd.fileno()
        return _fallocate(fd, mode, offset, len)
    fallocate.__doc__ = _fallocate.__doc__
except ImportError:
    def fallocate(fd, offset, len, mode=0):
        """ fallocate(2) or OSX equivalent was not found on this system"""
        warnings.warn("fallocate(2) or OSX equivalent was not found on this system")

try:
    from ._fallocate import posix_fallocate as _posix_fallocate
    from ._fallocate import posix_fadvise as _posix_fadvise
    from ._fallocate import POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL, POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, POSIX_FADV_DONTNEED
    def posix_fallocate(fd, offset, len):
        if isinstance(fd, file):
            fd = fd.fileno()
        return _possix_fallocate(fd, offset, len)
    posix_fallocate.__doc__ = _posix_fallocate.__doc__

    def posix_fadvise(fd, offset, len, advise):
        if isinstance(fd, file):
            fd = fd.fileno()
        return _posix_fadvise(fd, offset, len, advise)
    posix_fadvise.__doc__ = _posix_fadvise.__doc__
except ImportError:
    def posix_fallocate(fd, offset, len):
        """ posix_fallocate(3) was not found on this system """
        warnings.warn("posix_fallocate(3) was not found on this system")

    def posix_fadvise(fd, offset, len, advise):
        """ posix_advise(3) was not found on this system"""
        warnings.warn("posix_advise(3) was not found on this system")

