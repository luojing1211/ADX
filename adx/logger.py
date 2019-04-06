"""Logger.py defines the class for recording the parsed information and create
the indexing table.
"""
from astropy import log


def log_dir(dir_processors):
    """This is a simple logging function. It can be expand in the future.
    """
    for dp in dir_processors:
        dp.record_info()
        dp.update_log()
    return
