""" Directory_info.py defines the container of directory information """

import os
import json
from astropy import log
from astropy.time import Time
from astropy.utils import lazyproperty

from .adx_table import *


def read_config(config_file):
    # This is a temporary configuration reader.
    cf = open(config_file, 'r')
    return json.load(cf)


def load_table(table_path, table_type):
    pass

def init_table(table_template, table_type):
    table = table_type()
    return table.init_table(table_template)

class DataDirectory:
    """ DataDirectory is a class to collect information from the given data
    directory. Its subclasses will handled by a new DataDirectroy class.

    Parameter
    ---------
    dir_name: str
        The name of directory.

    table_file_exts: list
        The extensions of log table. Default ['.csv',]. This will help the table
        reader and writer.

    table_type: `ADX table type` class
        Date base table type. Default is the astropy table.

    Note
    ----
       Right now it only use .csv file as the table file. In the future it can
       be expend to other types.
    """
    def __init__(self, dir_path, table_file_ext='.csv',
                 table_type=AstropyAdxTable, config_file=None):
        self.path = os.path.abspath(dir_path)
        self.parent = os.path.basename(self.path)
        self.log_dir = os.path.join(self.path, "adx_log")
        if config_file is None:
            # use default config
            self.adx_config = os.path.join(self.log_dir, "config")
        else:
            self.adx_config = config_file
        self.table_ext = table_file_ext
        self.isadx = self.validate()
        self.master_table_path = os.path.join(self.log_dir, 'master' +
                                              self.table_ext)

        self.config = None
        self.master_table = None
        self.log_tables = []
        self.subdirs = []
        self.ext_category = {}
        # have all subdirectory
        for item in self.all_items:
            if not os.path.isdir(item):
                item_ext = os.path.splitext(item)[1].replace('.', '')
                if item_ext in self.ext_category.keys():
                    self.ext_category[item_ext].append(item)
                else:
                    self.ext_category[item_ext] = [item,]
            else:
                if os.path.basename(item) != os.path.basename(self.log_dir):
                    self.subdirs.append(item)

    def validate(self):
        """Check if this directory an adx logged data directory.
        """
        # Check if directory has config
        if os.path.exists(self.adx_config):
            return True
        else:
            return False

    def setup(self):
        self.config = read_config(self.adx_config)
        self.master_table = load_table(self.master_table_path,
                                       self.table_ext)
        self.log_tables = [tf for tf in os.listdir(self.log_dir) if
                           (tf.endswith(self.table_ext) and not
                            tf.startswith('master'))]

    @property
    def target_exts(self):
        return self.config['file_extensions']

    @property
    def all_items(self):
        return [os.path.join(self.path, item) for item in os.listdir(self.path)]

    @property
    def directory_modify_time(self):
        """Get the directory's newest modify time"""
        return os.path.getmtime(self.path)

    @property
    def next(self):
        return self.subdirs

    def get_parse_info(self, ext_name):
        try:
            return self.config[ext_name]
        except KeyError:
            raise ValueError("{} is not in the target extension list.")

    def get_ext_table(self, ext):
        pass

    def load_ext_table(self, ext):
        pass

    def mt_diff(self, ext):
        pass

#
#     def get_item_diff(self):
#         pass
#
#     @property
#     def history_modify_time(self):
#         """Get the modify time in the log"""
#         if self.dir_log == None:
#             return 0.0
#         else:
#             mt = [os.path.getmtime(x) for x in self.dir_log.files]
#             return mt
#
#
#     @property
#     def modify_time(self):
#         """Get the newest modify time"""
#         return os.path.getmtime(self.path)
#
#
#     def match_parser(self, item_path, parses):
#         """
#         Parameter
#         ---------
#         item: str
#             item path.
#         parsers : Dict
#             dict of parsers. The key is the extansions and the value is the list
#             of parsers that accepts the extensions.
#
#         Return
#         ------
#         cataloged
#         """
#         # First try to indentify the file type from the extensions
#         item_ext =  os.path.splitext(item_path)[1]
#         # Get all the parsers for checkin unknow extensions.
#         all_parsers = []
#         for plist in parsers.values():
#             all_parsers.append(plist)
#         all_parsers = list(set(all_parsers))
#         cateloged = True
#         if item_ext not in parses.keys():
#             for pp in plist:
#                 if pp.check_type(item_path):
#                     if pp.name not in self.keys():
#                          self[pp.name] = [item_path,]
#                     else:
#                          self[pp.name].append(item_path)
#                 else:
#                     cateloged = False
#         else:
#             for p in parses[ext]:
#                 if p.check_type(item_path):
#                     if p.name not in self.keys():
#                          self[p.name] = [item_path,]
#                     else:
#                          self[p.name].append(item_path)
#                     break
#                 else:
#                     cateloged = False
#         return cateloged
#
#     def update_log(self):
#         """update the overall log in the directory """
#         pass
#
#     def record_info(self):
#         """Log the information to different tabfrom collections.abc import Iterableles """
#         pass
#
#
def init_adx_dir(dir_path, target_file_exts):
    """ Setup a directory for adx data indexing

    Parameters
    ----------
    dir_path: str
        Target directory path.

    target_file_exts: str list
        The file extensions for indexing.

    recursive: bool, optional
        If allow adx navigate to the subdirectory recursively. Default is True.
    """
    adx_dir = os.path.join(dir_path, 'adx_log')
    adx_config = os.path.join(adx_dir, 'config')
    if isinstance(target_file_exts, str):
        exts = set([target_file_exts,])
    elif isinstance(target_file_exts, (list, tuple, set)):
        exts = set(target_file_exts)
    else:
        raise ValueError("'target_file_exts' only accepts 'str', 'list', "
                         "'tuple', or 'set'.")
    if not os.path.exists(adx_dir):
        os.mkdir(adx_dir)

    # add default parse information from file
    ext_config = {}
    for ext in exts:
        ext_config[ext] = {'parse_info': ['mtime',]}

    init_time = Time.now().iso
    config_info = {'path': adx_dir,
                   'init_time_utc': init_time,
                   'file_extensions': list(exts)}
    config_info.update(ext_config)
    f = open(adx_config, "w")
    json.dump(config_info, f, sort_keys=True, indent=4, separators=(',', ': '))
    return
