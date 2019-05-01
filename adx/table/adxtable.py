class ADXTableBase(object):
    """Base class for storing calculated metrics or data results.
    
    Parameters
    ----------
    name : str
        name of table
    tableType: str
        table type
    tablePath : str, optional
        Path of target table file. 

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

    def __init__(self, name, tableType, tablePath=None):
        self._name = name
        self._tabletype = tableType
        if tablePath is None:
            self.tablepath = None
            self.table_ext = ''
        else:
            self.tablepath = tablePath
            _, ext = os.path.splitext(tablePath)
            self.table_ext = ext
            #self.load(tablePath)

    @property
    def tabletype(self):
        return self._tabletype

    @property
    def tablepath(self):
        return self._tablepath
    
    @tablepath.setter
    def tablepath(self, t):
        self._tablepath = t

    @property
    def name(self):
        return self._name

    def close(self):
        """close ADXTable object
        """
        raise NotImplementedError, "user defined method"
    
    def update(self, newResult):
        """update ADX table with new result
        """
        raise NotImplementedError, "user defined method"

    def loadfile(self, loadpath):
        """load `loadpath` as an ADX table.
        """
        raise NotImplementedError, "user defined method"
    
    def load(self, dataDir):
        """load ADXTable info from data directory path.

        Parameters
        ----------
        dataDir : str
            path to data directory, parent of ".adx/"

        Notes
        -----
        ADXTable will be opened by looking for a local table in
        `dataDir`/.adx/<table name>.adx.<table extension>

        Actions if the directory '.adx' or the table file do not exist are 
        user-defined.
        """
        fp = os.path.join(dataDir, '.adx', self.name + self.table_ext)
        self.loadfile(fp)


