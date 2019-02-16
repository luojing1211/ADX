""" parser.py implements the parser base class, which defines the base API for
    different parser type.
"""

import os
from astropy import log


__all__ = ["ParserBase"]


class ParserBase:
    """Base class for all types of parser.

    ParserBase class defines the high-level API for the subclass of parser. It
    contains the wrapper methods that call the file type check functions and
    all the user defined parse functions.

    The Parser class is a callable class which returns all the information
    requested by the user.

    Parameters
    ----------
    file_type : str
        Type name.
    extensions: str or list
        All the acceptable file extensions.

    Atributes
    ---------
    parse_funs: tuple
        The request information name and the method/callable functions to get
        the information. The first element is the request information name (in
        ADX this attribute will be used as the database column name.), and the
        second value is the callable fucntions that parse the information.
        One should organize the parse functions accordingly. 
        The default is an empty tuple.
    """
    def __init__(self, file_type, extensions):
        self.file_type = file_type
        if isinstance(extensions, str):
            extensions = [extensions,]
        self.extensions = extensions
        self.parse_funcs = ()

    def __call__(self, filename, **kwargs):
        """ High-level parse_info method.

        Paremeters
        ----------
        filename : str
            Full path to the file.
        **kwargs :
            Addtional input to the parse functons.
        """
        if not self.check_type(filename):
            return None
        else:
            if parse_funcs == ():
                raise ValueError("Parser needs parse functions.")
            result = {}
            for k, f in self.parse_funs:
                result[k] = f(filename, **kwargs)
            return result

    def check_type(self, filename):
        """ User defined file type checker.

        Paremeter
            ---------
            filename : str
                The file name
            Return
            ------
            If the file belongs to the defined type, return True, otherwrise
            False.
        """
        raise  NotImplementedError
