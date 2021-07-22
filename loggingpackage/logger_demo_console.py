"""
Logger Demo
"""

import logging


class LoggerDemoConsole():
    def testLog(self):
        # create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__)
        logger.setLevel(logging.INFO)

        # create console handler and set Level to info
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        # create formatter
        formatters = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s %(message)s',
                                       datefmt='%d/%m/%Y %I:%M:%S %p')

        # add formatter to console handler -> chandler
        chandler.setFormatter(formatters)

        # add console handler to logger
        logger.addHandler(chandler)

        # logging messages
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")


demoConsole = LoggerDemoConsole()
demoConsole.testLog()
