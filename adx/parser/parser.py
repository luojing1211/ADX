""" parser.py implements the parser base class, which defines the base API for
    different parser type.
"""

import os
from astropy import log


__all__ = ["ParserBase",]


class ParserBase:
    """Base class for all types of parser.

    ParserBase class defines the high-level API for the subclass of parser. It
    contains the wrapper methods that call the item type check functions and
    all the user defined parse functions.

    The Parser class is a callable class which returns all the information
    requested by the user.

    Parameters
    ----------
    item_type : str
        Type name.
    extensions: str or list
        All the acceptable item extensions.
    reader_cls : class or callable, optional
        A reader class/function returns the object that provides the methods to
        help interpret the data. For instance, a simple reader is the `open()`
        function. The default is None
    reader_args: dict, optional
        The extra arguments that needed by the reader.

    Atributes
    ---------
    info_list: list
        The list of information that parser returns. This will be used in the
        logger.
    reader: instance
        An item instance provides the methods to interpret the data.
    """
    def __init__(self, name, extensions, reader_cls=None, reader_args={}):
        self.name = name
        if isinstance(extensions, str):
            extensions = [extensions,]
        self.extensions = extensions
        self.reader_cls = reader_cls
        self.reader_args = reader_args
        self.reader = None
        self.info_list = []
        self.type_checker =[]

    def __call__(self, itemnames, **kwargs):
        """ High-level parse_info method.

        Paremeters
        ----------
        itemname : list
            Full path to the items that in this parser type.
        **kwargs :
            Addtional input to the parse functons.

        Note
        ----
        This if for the general purpose, however, it can be redefined in the
        subclass.
        """
        raise NotImplementedError

    def check_type(self, itemname):
        """ User defined item type checker.

        Paremeter
            ---------
            itemname : str
                The item name
            Return
            ------
            If the item belongs to the defined type, return True, otherwrise
            False.
        """
        raise  NotImplementedError

    def get_reader(self, name):
        """ Help function to build the reader instance.
        """
        raise  NotImplementedError

    def add_checker(self, condition, priority=None):
        if priority is None:
            self.type_checker.append(condition)
        else:
            self.type_checker.insert(priority, condition)

    def add_parse_info(self, name, function, help=None, dtype=None):
        pass
