""" Directory_info.py defines the container of directory information """

import os
import json
from astropy import log
from astropy.time import Time


def read_config(config_file):
    cf = open(config_file, 'r')
    return json.load(cf)


class DataDirectory:
    """ DataDirectory is a class to collect information from the given data
    directory. Its subclasses will handled by a new DataDirectroy class.

    Parameter
    ---------
    dir_name: str
        The name of directory
    """
    def __init__(self, dir_path):
        self.path = os.path.abspath(dir_path)
        self.parent = os.path.basename(self.path)
        self.all_items = [os.path.join(self.path, item) for item in
                          os.listdir(self.path)]
        self.adx_dir = os.path.join(self.path, "adx_log")
        self.adx_config = os.path.join(self.adx_dir, "config")
        self.isadx = self.validate()
        if not self.isadx:
            self.config = None
        else:
            self.config = read_config(self.adx_config)
        self.subdirs = []
        # have all subdirectory
        for item in self.all_items:
            print(item)
            if os.path.isdir(item) and item != os.basname(self.adx_dir):
                self.subdirs.append(item)

    def validate(self):
        """Check if this directory an adx logged data directory.
        """
        # Check if directory has config
        if os.path.exists(self.adx_config):
            return True
        else:
            return False

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
