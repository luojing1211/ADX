"""sqliteTable.py
sqlite3 ADXTable implementation
"""

from .base import TableWrapper
import sqlite as sql
import os

class SqliteAdxTable(TableWrapper):
    """SQLite3 DB handler

    basic implementation of an ADX Table using sqlite3 as a
    backend.

    Parameters
    ----------
    fp : str
        Filepath to sqlite db file.
    name : str, optional
        Name of ADXTable implementation.

    """
    def __init__(self, table_path, write=False):
        super(SqliteAdxTable, self).__init__(table_path, write=False)
        self.tableMap = None
        self.sqlConn = None
        self.sqlCursor = None

    @property
    def sqlConn(self):
        return self._sqlConn

    @property
    def sqlCursor(self):
        return self._sqlCursor

    @property
    def tableMap(self):
        return self._tableMap

    @tableMap.setter
    def tableMap(self, tmap):
        """Set sqlite table map

        Parameters
        ----------
        tmap : tuple
            tuple defining table fields and their data types

        Notes
        -----
        The table map, `tmap`, should be be a tuple of field definition
        tuples. A field definition tuple should contain 2 elements
        in following structure `(field_name, field_dtype)`. For example,
        the table map for an ADXTable containing two fields could look like
        the following: (('date', 'text'), ('avg', 'real')).
        """

        self._tableMap = tmap

    def load(self, loadpath=None, create=False):
        """load sqlite db file as ADXTable

        Parameters
        ----------
        loadpath : str, optional
            Path to db file
        create : boo, optional
            If true then create new table if `loadpath` does not exist
            and `tableMap` has been set.
        """

        if loadpath is None:
            loadpath = self.tablepath

        if not os.path.isfile(loadpath):
            if create:
                # attempt to create this db file
                if self.tableMap:
                    table_fields = self.parse_field_list(self.tableMap)
                    sql_cmd = "CREATE TABLE adx ({})".format(table_fields)
                    self.db_connect(loadpath)
                    self.sqlCursor.execute(sql_cmd)
                    self.sqlConn.commit()
                else:
                    emsg = "cannot create new Sqlite ADX Table without \
                            a tablemap"
                    raise RuntimeError(emsg)
            else:
                emsg = "no such file: {}".format(loadpath)
                raise IOError(emsg)
        else:
            self.db_connect(loadpath)

    def db_connect(self, fp):
        """initiate sqlite3 db connection
        Set `self.sqlConn` and `self.sqlCursor` with sqlite3
        connection parameters.

        Parameters
        ----------
        fp : str
            File path to sqlite3 db file
        """
        conn = sql.connect(fp)
        cur = conn.cursor()

        self._sqlConn = conn
        self._sqlCursor = cur

    @staticmethod
    def parse_field_list(tmap):
        """parse table map field list

        Parameters
        ----------
        tmap : tuple
            tuple defining fieldnames and data types for sqlite db

        Returns
        -------
        tmap_str : str
            field value pairs as a string that can be used to
            create a table as an sql query
        """

        s = ''
        N = len(tmap)
        for i in range(N):
            if i:
                s += ', '
            f,v = tmap[i]
            s += "{} {}".format(f, v)
        return s

    def close(self):
        """close the db file
        """
        self.sqlConn.close()

    def update(self, newResult):
        """Update sqlite table

        Parameters
        ----------
        newResult : tuple
            results to be updated to latest record in database.

        Notes
        -----
            `newResult` must be a tuple of (field, value) pairs
        """
        fields = self.parse_field_list(newResult)
        query = "UPDATE adx SET "
        pass
