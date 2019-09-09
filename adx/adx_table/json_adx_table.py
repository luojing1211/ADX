"""json_adx.py
simple json ADXTable implementation
"""
from .base import TableWrapper
import json
import os

class JsonAdxTable(TableWrapper):
    """Simple Json table
    """
    def __init__(self, table_path, write=False):
        super(JsonAdxTable, self).__init__(table_path, write=write)

    def validate(self):
        super(JsonAdxTable, self).validate()
        if self.table_ext == '.json':
            raise ValueError("Table file {} is not a JSON table.".format(self.path))

    def close(self):
        """close all open files
        """
        pass

    def update(self, newValues):
        """Update data record.

        Parameters
        ----------
        newValues : dict
            fields to be updated with new values
        """
        if not isinstance(newValues, dict):
            raise TypeError("expected new values as a dictionary")

        for k,v in newValues.iteritems():
            self.data[k] = v

        self.save()

    def loadfile(self, fp=None):
        """load ADXTable json file into memory
        If file does not exist then load empty dictionary.

        Parameters
        ----------
        fp : str, optional
            filepath to table file to be loaded
        """

        if fp is None:
            fp = self.tablepath

        if os.path.isfile(fp):
            with open(fp, 'r') as f:
                self.data = json.load(f)
        else:
            self.tablepath = fp
            self.data = json.loads('{}')

    def save(self):
        """save internal data to disk
        """

        with open(self.tablepath, 'w') as fp:
            json.dump(self.data, fp)


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, datum):
        if not isinstance(datum, dict):
            raise TypeError("expected dictionary")
        self._data = datum
