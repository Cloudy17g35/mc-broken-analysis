import logging
import sys


class Logger(object):
    
    def __init__(self, file, format="%(asctime)s | %(levelname)s | %(message)s", level=logging.INFO):
        # Initial construct.
        self.format = format
        self.level = level
        self.file = file

        # Logger config for file
        self.file_handler = logging.FileHandler(self.file)
        self.file_handler.setLevel(logging.INFO)
        fileformat = logging.Formatter("%(asctime)s [%(levelname)s] - [%(filename)s >"
                             " %(funcName)s() > %(lineno)s] - %(message)s")
        self.file_handler.setFormatter(fileformat)
        
        # logger for console
        self.console_logger = logging.StreamHandler(sys.stdout)
        self.console_logger.setLevel(logging.INFO)
        console_format = logging.Formatter(self.format)
        self.console_logger.setFormatter(console_format)

        # Complete logging config.
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.level)
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_logger)
        
        
    def info(self, msg, extra=None):
        self.logger.info(msg, extra=extra)

    def error(self, msg, extra=None):
        self.logger.error(msg, extra=extra)

    def debug(self, msg, extra=None):
        self.logger.debug(msg, extra=extra)

    def warn(self, msg, extra=None):
        self.logger.warn(msg, extra=extra)

