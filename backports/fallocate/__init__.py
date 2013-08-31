
__version__ = "1.0"

try:
    from ._fallocate import fallocate
except ImportError:
    pass
try:
    from ._fallocate import posix_fallocate, posix_fadvise
    from ._fallocate import POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL, POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED, POSIX_FADV_DONTNEED
except ImportError:
    pass

