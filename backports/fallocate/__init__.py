
__version__ = "1.0"

try:
    from ._fallocate import fallocate as real_fallocate
    def fallocate(fd, mode, offset, len):
        if isinstance(fd, file):
            fd = fd.fileno()
        return real_fallocate(fd, mode, offset, len)
    fallocate.__doc__ = real_fallocate.__doc__
except ImportError:
    pass

try:
    from ._fallocate import posix_fallocate as real_posix_fallocate
    from ._fallocate import posix_fadvise as real_posix_fadvise
    from ._fallocate import POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL, POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, POSIX_FADV_DONTNEED
    def posix_fallocate(fd, offset, len):
        if isinstance(fd, file):
            fd = fd.fileno()
        return real_possix_fallocate(fd, offset, len)
    posix_fallocate.__doc__ = real_posix_fallocate.__doc__

    def posix_fadvise(fd, offset, len, advice):
        if isinstance(fd, file):
            fd = fd.fileno()
        return real_posix_fadvise(fd, offset, len, advice)
    posix_fadvise.__doc__ = real_posix_fadvise.__doc__
except ImportError:
    pass

