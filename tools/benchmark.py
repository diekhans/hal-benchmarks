# some shared functions

import datetime
import os.path
from collections import namedtuple

class RunMeta(namedtuple("RunMeta", ("dset", "fmt", "protocol"))):
    __slots__ = ()

def isoday():
    return datetime.datetime.now().strftime('%Y-%m-%d')

def parseTimeFileMeta(timeLog):
    # 10plusway-mapq.hdf5_gzip2.local.nt0.time
    # 10plusway-mapq.mmap.local.nt0.time
    fileName = os.path.basename(timeLog)
    try:
        dset, fmt, protocol, ext = fileName.split('.')
    except Exception as ex:
        raise Exception("Error: {} parsing {}".format(str(ex), fileName))
    return RunMeta(dset, fmt, protocol)
