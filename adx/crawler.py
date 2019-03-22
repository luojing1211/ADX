"""crawler.py defines the ADX crawler and supporting functions.
   The functionality of ADX crawler.
   1. Navigate through one directory
   2. Check item type
   3. Log data file information.
"""

import os


class Crawler:
    """ Crawler is designed to traverse all the items including the
        subdirectories in a directory. After the crawling, it returns 
        a list of target items and their parser.

        Parameter
        ---------
        dir_name : str
            Directory name
        parsers : list
            A list of `Pareser object` for each item type.
        recusive: bool, optional
            The flag that tells if the crawler to go through the subdirecotries.
            The default is 'True'.
        batch : int, optional
            Sets the size of the batch which are processed at once. 

        Note
        ----
        Crawler only parses the item types that have the `Parser` object
        provided.
    """
    def __init__(self, dir_name, parsers, recusive=True):
        self.root_dir = dir_name
        self.parsers = parses
        # If the parser_template does not include the customer defined parser,
        # it will add the default directory parser.
        if 'directory' not in self.parser_template:
            self.parser_template.update({'directory': ParserDir})
        self.recusive = recusive
        self.cur_location = dir_name
        self.cur_dir_info = ParserDir(self.cur_dir)
        self.visited = [self.cur_location,]
        self.set_up()

    def set_up(self):
        """ This function prepares the crawler. It does the following steps:
        1. Gather the item types information for the parsers.
        2. Build the extension map
        ....
        """
        self.target_types = []
        self.ext_map = {}
        # get all the types and build the extension map.
        for p in self.parsers:
            self.target_types.append(p.item_type)
            for ext in p.extensions:
                if ext not in self.ext_map.keys():
                    self.ext_map[ext] = [p,]
                else:
                    self.ext_map.append(p)

    def _check_ext(self, item):
        """ Check item's extension.

            Parameter
            ---------
            item : str
                The full path to the item.

            Return
            ------
            The item extension as a string. If the item is a directory, it
            returns 'directory'.
        """
        if os.path.isdir(item):
            return 'directory'
        else:
            itemname, item_type = os.path.splitext(item)
            return item_type

    def get_parser(self, item):
        """Get the right parser for the item according to the item type. The
        item type will be indentified by item extension checking and parser's
        double checking.

        Parameter
        ---------
        item : str
            The full path to the item.
        Return
        ------
        The Parser class
        """
        item_ext = self._check_ext(item)
        if item_ext not in self.ext_map:
            return
        else:
            for tp in self.ext_map(item_ext):
                if tp.check_type(item):
                    return tp
                else:
                    return

    # TODO add functions to read the old item lists and not crawl the loged
    # items

    def crawl_dir(self, recusive=True):
        pass
