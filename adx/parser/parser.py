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
    parse_funs: list of tuple
        The request information name and the method/callable functions to get
        the information. The first element is the request information name (in
        ADX this attribute will be used as the database column name.), and the
        second value is the callable fucntions that parse the information.
        One should organize the parse functions accordingly.
        The default is an empty list.
    reader: instance
        An item instance provides the methods to interpret the data.
    """
    def __init__(self, item_type, extensions, reader_cls=None, reader_args={}):
        self.item_type = item_type
        if isinstance(extensions, str):
            extensions = [extensions,]
        self.extensions = extensions
        self.reader_cls = reader_cls
        self.reader_args = reader_args
        self.reader = None
        self.parse_funcs = []

    def __call__(self, itemname, **kwargs):
        """ High-level parse_info method.

        Paremeters
        ----------
        itemname : str
            Full path to the item.
        **kwargs :
            Addtional input to the parse functons.

        Note
        ----
        This if for the general purpose, however, it can be redefined in the
        subclass.
        """
        if not self.check_type(itemname):
            return None
        else:
            if parse_funcs == []:
                raise ValueError("Parser needs parse functions.")
            result = {}
            for k, f in self.parse_funs:
                result[k] = f(itemname, **kwargs)
            return result

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
