"""
Logging Format
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', level=logging.DEBUG, datefmt='%d/%m/%Y %I:%M:%S %p')
logging.warning("Warning message")
logging.info("Info message")
logging.error("Error message")