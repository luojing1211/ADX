"""crawler.py defines the ADX crawler and supporting functions.
   The functionality of ADX crawler.
   1. Navigate through the target directory
   2.

"""

import os


class DirProcessor(dict):
    """ DirProcessor is a class to collect information from the directory,
    including file types and file numbers.

    Parameter
    ---------
    dir_name: str
        The name of directory
    """
    def __init__(self, dir_path, parent=None, dir_log=None):
        self.path = os.abspath(dir_path)
        self.parent = parent
        self.dir_log = dir_log # Here needs a function of reading the dir_log
        self.all_items = [os.path.join(self.path, item) for item in os.listdir()]
        self.update = True # This is a flag for the parser.
        self.update({'unknown': [], 'uncate':[], 'directory':[])
        self.setup()

    def setup(self):
        # Check modify time
        if self.modify_time < self.history_modify_time:
            self.update = False
        # setup all the files.
        for item in self.all_items:
            # Get all the subdirectories
            if os.isidir(item):
                self['directory'].append(item)

    @property
    def history_modify_time(self):
        """Get the modify time in the log"""
        if self.dir_log = None:
            return 0.0
        else:
            mt = [os.path.getmtime(x) for x in self.dir_log.files]
            return mt

    @property
    def modify_time(self):
        """Get the newest modify time"""
        return os.path.getmtime(self.path)


    def match_parser(self, item_path, parses):
        """
        Parameter
        ---------
        item: str
            item path.
        parsers : Dict
            dict of parsers. The key is the extansions and the value is the list
            of parsers that accepts the extensions.

        Return
        ------
        cataloged
        """
        # First try to indentify the file type from the extensions
        item_ext =  os.path.splitext(item_path)[1]
        # Get all the parsers for checkin unknow extensions.
        all_parsers = []
        for plist in parsers.values()
            all_parsers.append(plist)
        all_parsers = list(set(all_parsers))
        cateloged = True
        if item_ext not in parses.keys():
            for pp in plist:
                if pp.check_type(item_path):
                    if pp.name not in self.keys():
                         self[pp.name] = [item_path,]
                    else:
                         self[pp.name].append(item_path)
                else:
                    cateloged = False
        else:
            for p in parses[ext]:
                if p.check_type(item_path):
                    if p.name not in self.keys():
                         self[p.name] = [item_path,]
                    else:
                         self[p.name].append(item_path)
                    break
                else:
                    cateloged = False
        return cateloged

    def update_log(self):
        """update the overall log in the directory """
        pass

    def record_info(self):
        """Log the information to different tables """
        pass

class Crawler:
    """ Crawler is designed to traverse all the items including the
        subdirectories in a directory. After the crawling, it returns a list of
        target files and their parser.

        Parameter
        ---------
        dir_name : str
            Directory name
        parsers : list
            A list of `Pareser object` for each item type.
        log_file: str
            The name of log_file

        Return
        ------
        A list of DirProcessors. These processors has the parser information so
        it can be sent to the logging function directly.
        Note
        ----
        Crawler only parses the item types that have the `Parser` object
        provided.
    """
    def __init__(self, dir_name, parsers, log_file=None):
        self.root_dir = DirProcessor(dir_name, log_file=None)
        self.parsers = parsers

    @property
    def ext_map(self):
        ext_map = {}
        for p in self.parsers:
            for e in p.extensions:
                if e not in ext_map.keys():
                    ext_map[e] = [p,]
                else:
                    ext_map[e].append(p)
        return ext_map

    def walk(self):
        # use DirProcessor['directory'] as linker to the next level.
        pass
