"""astropy_adx_table.py defines the API class for astropy table that could
interact with the general ADX API.
"""
import os
import numpy as np
from astropy.table import Table
from astropy.io import ascii

from .base import TableWrapper

class AstropyAdxTable(TableWrapper):
    """ AstropyAdxTable class is the API class for ADX interacting with the
    astropy table.

    Parameters
    ----------
    table : `astropy Table` object, optional.
        Input astropy table, optional.
    in_table_path: str, optional.
        Input table file path.
    """
    def __init__(table=None, in_table_path=None, table_template={}, format=None):
        super().__init__(table, in_table_path, table_template)
        self.format = format

    def validate(self):
        if self.table is not None:
            if not isinstance(self.table, Table):
                 raise ValueError('Input table is not an astropy table.')

    def read_table(self, path):
        """Load an ADX table from the path.
        """
        if self.format is None:
            self.format = os.path.splitext(path)
        table = ascii.read(path, format=self.format.replace('.', ''),
                           fast_reader=True)
        return table

    def init_table(self, template):
        """Initial a table from the columns.
        """
        columns = ['index', ] + list(template.keys())
        dtypes = [int,] + list(template.values())
        self.table = Table(names=columns, dtype=dtypes)

    def get_entry(self, condition):
        index = np.where(condition)
        return self.table[index]
