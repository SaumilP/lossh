"""
Utility versions
"""
import sys

__project__ = "lossh"
__version__ = "0.0.1"

def print_version():
    sv = sys.version_info
    py_version = "{}.{}.{}".format(sv.major, sv.minor, sv.micro)
    version_parts = __version__.split(".")
    s = "{} version: [{}], Python {}".format(__project__, __version__, py_version)
    s += "\nMajor Version: {} (breaking changes)".format(version_parts[0])
    s += "\nMior Version: {} (extra changes)".format(version_parts[1])
    s += "\nMicro Version: {} (commit counts)".format(version_parts[2])
    return s
