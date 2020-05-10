from .base import *

DEBUG = FALSE

try:
    from .local import *
except ImportError:
    pass
