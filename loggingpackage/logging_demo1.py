"""
Logging Demo 1
Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("Warning message")
logging.info("Info message")
logging.error("Error message")