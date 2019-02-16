"""Logger.py defines the class for recording the parsed information and create
the indexing table.
"""
from astropy import log


class Logger:
    """Logger class is designed to record the file or directory information to
    a data table. A logger operates on a list of files (with full path) and the
    associated file parser. The output file can be customerized by the user

    Parameters
    ----------
    target_items : dict
       The items need to be parsed. The key is the full path to the item, and
       the value is the parser for the item type.
    """
    def __init__(self, target_items):
        self.target_items = target_items
        self.set_up_table()

    @property
    def items(self):
        return list(self.target_items.keys())

    @property
    def parsers(self):
        return list(set(self.target_items.keys()))

    @property
    def types(self):
        parsers = list(set(self.target_items.keys()))
        t = [p.file_type for p in parsers]
        return t

    def set_up_table(self):
        self.tables_cols = {}
        for prs in self.parsers:
            self.tables_cols[prs] = [pf[0] for pf in prs.parse_funcs]

    def get_info_entry(self, item, parser):
        """ Parse the item information following the table column.
        """
        info  = parser(item)
        entry = ()
        for tc in self.tables_cols[parser.file_type]:
            entry += (info[tc],)
        return entry

    def log_info(self):
        pass

    def write_info(self):
        pass 
