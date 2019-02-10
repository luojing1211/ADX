"""crawler.py defines the ADX crawler and supporting functions.
   The functionality of ADX crawler.
   1. Navigate through one directory
   2. Check item type
   3. Log data file information.
"""

import os
from .parser import ParserDir


class Crawler:
    """ Crawler is designed to traverse and log all the items including the
        subdirectories in a directory.

        Parameter
        ---------
        dir_name : str
            Directory name
        parser_template : dict
            The template functions for parsing one type of files. The key is the
            file type name and the value is the Parser subclass of the same file
            type.
        recusive: bool, optional
            The flag that tells if the crawler to go through the subdirecotries.
            The default is 'True'.

        Note
        ----
        Crawler only parses the file types that have parser_template provided.
    """
    def __init__(self, dir_name, parser_template, recusive=True):
        self.root_dir = dir_name
        self.parser_template = parse_template
        # If the parser_template does not include the customer defined parser,
        # it will add the default directory parser.
        if 'directory' not in self.parser_template:
            self.parser_template.update({'directory': ParserDir})
        self.recusive = recusive
        self.cur_location = dir_name
        self.cur_dir_info = ParserDir(self.cur_dir)
        self.visited = [self.cur_location,]

    def check_type(self, item, file_type_map={}, sign_lenght=32):
        """ Check item type

            Parameter
            ---------
            item : str
                The full path to the item.
            file_type_map: dict, optional
                The file type identifier map. The key is the file signature and
                the value is file type name. If the file_type_map is not
                provided, the file will be identified by the file extensions.
            sign_lenght : int, optinal
                The maximum file signature length.

            Return
            ------
            The item type.
        """
        if os.path.isdir(item):
            return 'directory'
        else:
            f = open(item, "rb")
            sign = str(f.read(sign_lenght))
            file_type = ""
            for k, v in file_type_map.items():
                if sign.startswith(k):
                    file_type = v
            if file_type == "":
                # Can not indentify file from the file type map
                # Then get file type from the file extensions
                filename, file_type = os.path.splitext(item)
            return file_type

    def crawl_dir(self, recusive=True):
        pass
