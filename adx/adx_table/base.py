""" 'base.py' defines the base classs for ADX table. Different types of tables
are derived from the base class.
"""
import os


class AdxTableBase(object):
    """Base class for adx table.

    ADX table are designed for the indexing the astronomical data file meta data
    and for querying the data files.

    Parameters
    ----------
    table_path: str
        The path to the table file.

    wirte: bool, optional
        The flag for writing the table. If true, adx will create a new file when
        the file does not exist, otherwrise it will over write the old table
        file. Defaul is False.

    Attributes
    ----------
    _tablepath : str
        Path to table file.

    Methods
    _______
    close()
        Clean up and close table file object.
    update(<user defined result object>)
        User defined object (or abstract data type) for passing results
        to implemented ADXTable object.
    load(tablepath, create=False)
        Load ADXTable file
    """

    def __init__(self, table_path, write=False):
        self.path = table_path
        self.write = write
        self.validate()
        # Get the extension and the name
        name_fields  = os.path.splitext(self.path)
        self.table_name = os.path.basename(name_fields[0])
        self.table_ext = name_fields[1]

    def validate(self):
        """Validation for the adx table. If the path does not exist, it will
        check write attribute. When write is true, it will set to create a new
        table.
        """
        if not os.path.exists(self.path):
            # check write flag
            if not self.write:
                raise FileNotFoundError("Table file '{}'' is not found. For "
                                        "creating a new file please set the "
                                        "write flag to 'True'.".format(self.path))
        else:
            if not os.path.isfile(self.path):
                raise ValueError("'{}' is not a file.".format(self.path))

    def read(self):
        """Load an ADX table from the path.
        """
        raise NotImplementedError("Defined in the subclass method.")

    def write(self, path=None):
        """Write out the ADX table.

        Parameter
        ---------
        path: str, optional
           The output file path.
        """
        if path is None:
            path = self.path
        if self.write:
            self._write(path)

    def _write(self, path):
        raise NotImplementedError("Defined in the subclass method.")

    def close(self):
        """close ADXTable object
        """
        raise NotImplementedError("Defined in the subclass method.")
