import os
from . import logs, tracks, boto3

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

DEEPRACER_UTILS_ROOT = os.path.dirname(os.path.abspath(__file__))
