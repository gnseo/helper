"""
create log instance
"""
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

log.info("================================")
log.info("{0} of {1} is running.".format(
    "__init__" if __package__ == __name__ else __name__,
    __package__
))

"""
collect packages into "pip" folder to simplify source code tree and allow Python to import packages as usual
"""
import sys
import pathlib

def pipdir(filepath, pipdir):
  current_dir = pathlib.Path(filepath).parent
  log.debug("this is current_dir: %s" % current_dir)
  sys.path.insert(0, '{0}/{1}'.format(current_dir,pipdir))

from . import *

# for attr in dir():
#   print(attr, getattr(sys.modules[__name__],attr))
