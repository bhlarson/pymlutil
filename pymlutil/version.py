import sys, os
sys.path.insert(0, os.path.abspath('.'))
from pymlutil.jsonutil import ReadDict

__version__ = ReadDict('config/build.yaml')['version']

def version():
    return __version__