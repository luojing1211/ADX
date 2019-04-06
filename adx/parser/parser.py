""" parser.py implements the parser base class, which defines the base API for
    different parser type.
"""

import os
from astropy import log


__all__ = ["ParserBase", "DirParser"]


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

        Note
        ----
        This if for the general purpose, however, it can be redefined in the
        subclass.
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


class DirParser(ParserBase):
    """ A parser class for the directory. The directory parser is designed to
    collect the over all information from a directory. It is able to read the old
    directory logs, if provided, and provide updates on the directory
    information. If the log is not provided, it will create a directory log
    based on the current status.
    """
    def __init__(self):
        super().__init__('directory', 'directory')

    def set_up(self):
        pass

    def check_type(self, filename):
        return os.path.isdir(filename)

    def read_logs(self, input_log=None, log_format=None):
        pass

    def cur_item_num(self, dir_name):
        return len(os.path.listdir(dir_name))

    def last_update(self, dir_name):
        pass
