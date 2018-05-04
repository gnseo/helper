"""
create logger instance
"""
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

"""
collect packages into "pip" folder to simplify source code tree and allow Python to import packages as usual
"""
import sys
import pathlib

current_dir = pathlib.Path(__file__).parent
print("this is current_dir: %s" % current_dir)
sys.path.insert(0, '%s/pip' % current_dir)
