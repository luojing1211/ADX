""" dirparser defines the parser for the directory and the helper class for
for reading.
"""
from .parser import ParserBase
from ..logger import Logger
import os

__all__ = ['DirReader', 'DirParser']


class DirReader:
    """This a helper class that designed to collect the exist information from
    a directory.

    Parameters
    dir_path: str
        The directory path.
    """
    def __init__(self, dir_path):
        self.dir_path = os.path.abspath(dir_path)
        self.all_items = os.path.listdir(self.dir_path)

    def get_items_mtime(self):
        """Get all items' modified time.
        """
        result = {}
        for ait in self.all_items:
            full_path = os.path.join(self.dir_path, ait)
            result[ait] = os.path.getmtime(full_path)
        return result

    def get_dir_mtime(self):
        its_mtime = self.get_item_mtime()
        return max(its_mtime.values())

    def get_items_size(self):
        result = {}
        for ait in self.all_items:
            full_path = os.path.join(self.dir_path, ait)
            result[ait] = os.path.getsize(full_path)
        return result

    def get_dir_size(self):
        its_size = self.get_items_size()
        return sum(its_size.values())

    def get_logs(self, ):
        pass
    def read_log(self, log_name):
        pass

class DirParser(ParserBase):
    """ A parser class for the directory. The directory parser is designed to
    collect the over all information from a directory. It is able to read the
    old directory logs, if provided, and provide updates on the directory
    information. If the log is not provided, it will create a directory log
    based on the current status.
    """
    def __init__(self, extra_funcs={}:
        super().__init__('directory', 'directory', DirReader)
        self.extra_funcs = extra_funcs

    def set_up(self):
        """ Organize the parese_funcs
        """
        for ef in self.extra_funcs.items():
            self.parse_funcs.append(ef)

    def check_type(self, itemname):
        return os.path.isdir(itemname)

    def get_reader(self, itemname):
        self.reader = self.reader_cls(itemname)
