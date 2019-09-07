""" astropy_adx_table.py defines the class for reading ADX table to astropy
table format.
"""

from astropy.io import ascii

from .base import AdxTableBase


class AstropyAdxTable(AdxTableBase):
    """ AstropyAdxTable is designed for reading the ADX tables to astropy table
    format.

    Parameters
    ----------
    table_path: str
        The path to the table file.

    wirte: bool, optional
        The flag for writing the table. If true, adx will create a new file when
        the file does not exist, otherwrise it will over write the old table
        file. Defaul is False.
    """
    def __init__(self, table_path, write=False):
        super(AstropyAdxTable, self).__init__(table_path, write=write)

    def read_table(self):
        """Read an ADX table file to astropy table.
        """
        data = ascii.read(lines, format=self.ext.replace('.', ''),
                          fast_reader=True)
        return data

    def _write(self, path, **kwargs):
        ascii.write(self.data, path, format=self.ext.replace('.', ''),
                    overwrite=True, **kwargs)
