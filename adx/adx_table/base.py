""" 'base.py' defines the base classs for ADX table. Different types of tables
are derived from the base class.
"""
import os

# TODO make sure the table can be initizialed independly and we can combine the
# tables.
class TableWrapper(object):
    """Base class for adx table.

    ADX table are designed for the indexing the astronomical data file meta data
    and for querying the data files.

    Parameters
    ----------
    table : table object
        The table for wrappering.

    table_path: str
        The path to the table file.

    table_template: dict, optional
        The template to initilze a new table.

    Methods
    -------
    close()
        Clean up and close table file object.
    update(<user defined result object>)
        User defined object (or abstract data type) for passing results
        to implemented ADXTable object.
    load(tablepath, create=False)
        Load ADXTable file
    """

    def __init__(self, table=None, in_table_path=None, table_template={}):
        self.table = table
        self.in_table_path = in_table_path
        self.table_template = table_template
        # if table is not given check other options
        if self.table is None:
            if self.in_table_path is not None:
                # Load table from path
                self.table = self.read_table(self.in_table_path)
            else:
                self.table = self.init_table(self.table_template)

    def __getattr__(self, name):
        try:
            # Try to get the attribute from the wapper. Otherwrise get it from
            # the table attribute.
            if six.PY2:
                return super(TableWrapper, self).__getattribute__(name)
            else:
                return super().__getattribute__(name)
        except AttributeError:
            try:
                return self.table.__getattribute__(name)
            except:
                raise AttributeError("Can not find the attribute {}.".format(name))

    def read_table(self, path):
        """Load an ADX table from the path.
        """
        raise NotImplementedError("Defined in the subclass method.")

    def write_table(self, path, overwrite=False):
        """Write out the ADX table.

        Parameter
        ---------
        path: str
           The output file path.
        """
        raise NotImplementedError("Defined in the subclass method.")

    def close_table(self):
        """close ADXTable object
        """
        del self.table

    def get_entry(self, condition):
        return NotImplementedError("Defined in the subclass method.")

    # def __add__(self, other_table):
