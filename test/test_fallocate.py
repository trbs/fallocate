#!/usr/bin/env python

import os
import platform
import tempfile
from fallocate import fallocate

def simple_fallocate_1kb_test():
    with tempfile.NamedTemporaryFile() as ntf:
        assert os.path.getsize(ntf.name) == 0
        fallocate(ntf, 0, 1024)
        assert os.path.getsize(ntf.name) == 1024

def simple_fallocate_1mb_test():
    with tempfile.NamedTemporaryFile() as ntf:
        assert os.path.getsize(ntf.name) == 0
        fallocate(ntf, 0, 1024*1024)
        assert os.path.getsize(ntf.name) == 1024*1024

if platform.system() == "Linux":
    from fallocate import FALLOC_FL_KEEP_SIZE, FALLOC_FL_PUNCH_HOLE
    def fallocate_punch_hole_test():
        with tempfile.NamedTemporaryFile() as ntf:
            assert os.path.getsize(ntf.name) == 0
            ntf.write(b"Hello World")
            ntf.flush()
            ntf.seek(0)
            assert ntf.read() == b"Hello World"
            fallocate(ntf.fileno(), 6, 4, mode=FALLOC_FL_KEEP_SIZE | FALLOC_FL_PUNCH_HOLE)
            ntf.seek(0)
            assert ntf.read() == b"Hello \x00\x00\x00\x00d"
