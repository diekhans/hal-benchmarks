# some shared functions

import datetime
import os.path
from collections import namedtuple

class RunMeta(namedtuple("RunMeta", ("dset", "fmt", "protocol"))):
    __slots__ = ()

def isoday():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def parseTimeFileMeta(timeLog):
    # 10plusway-mapq.hdf5_gzip2.local.1.time
    # 10plusway-mapq.mmap.local.1.time
    fileName = os.path.basename(timeLog)
    dset, fmt, protocol, run, ext = fileName.split('.')
    return RunMeta(dset, fmt, protocol)
