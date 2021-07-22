"""
Logger Demo
"""

import logging
import logging.config


class LoggerDemoConf:
    def testLog(self):
        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerDemoConf.__name__)

        # logging messages
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")


demoConf = LoggerDemoConf()
demoConf.testLog()