"""crawler.py defines the ADX crawler and supporting functions.
   The functionality of ADX crawler.
   1. Navigate through the target directory
   2.

"""



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
