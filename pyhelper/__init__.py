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

"""
show all objects including functions
"""
# for attr in dir():
#   print(attr, getattr(sys.modules[__name__],attr))

"""
complex encorder for json data
"""
import json
from datetime import date, datetime
from decimal import Decimal

class ComplexEncoder(json.JSONEncoder):
  def default(self, obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
      return obj.isoformat()
    elif isinstance(obj, Decimal):
      return str(obj)

    try:
      # Let the base class default method raise the TypeError
      return json.JSONEncoder.default(self, obj)
    except TypeError as te:
      raise TypeError("type:{0} - message:{1}".format(type(obj), repr(te.args)))
    # finally:
    #   return encoded
