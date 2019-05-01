class FileParserBase(object):
    """Parser parent class
    This class should be inherited to implement user-defined logic
    for the purposes of reading and calculating metrics to be stored
    in ADX tables.
    
    Attributes
    ----------
    filters : list
        user-defined TypeFilter objects.     
    tables : list 
        list of user-defined ADXTable objects
    targets : list 
        list of target file paths 
        
    Methods
    -------
    filter_targets()
        Iteratively apply TypeFilters in `self.filters` to targets listed in
        `self.targets` to determine which candidate targets apply to this 
        parser instance.
    run()
        Parse target files and execute user-defined file-specific logic.
    ls_filters()
        return list of filters registered in this FileParser
    """

    def __init__(self):
        self._filters = [] 
        self._tables = [] 
        self._targets = [] 

    @property
    def tables(self):
        """Internal list of ADX tables.
        """
        return self._tables

    @tables.setter
    def tables(self, newTables):
        """Set internal list of ADX Tables
        """
        
        # make sure `newTables` is an iterable object
        if not hasattr(newTables, "__iter__"):
            newTables = list(newTables)

        for t in newTables:
            if not isinstance(t, ADXTable):
                errmsg = "all tables must be an instance of ADXTable"
                raise TypeError(errmsg)
        self._tables = list(newTables)
   
    @property
    def targets(self):
        """Internal list of ADX targets
        """
        return self._targets

    @targets.setter
    def targets(self, newTargets):
        """set a new target list
        """
        for t in newTargets:
            if not os.path.isfile(t):
                raise IOError("file must be a regular file: {}".format(t))
        self._targets = list(newTargets)

    @property
    def filters(self):
        """internal list of TypeFilters
        """
        return self._filters
    
    def ls_filters(self):
        """return list of registered filtered names
        """
        return [f.name for f in self.filters]
   
    @filters.setter
    def filters(self, newFilters):
        """set new filter list
        
        Parameters
        ---------- 
        newFilters : list
            List of TypeFilters to be applied by this parser.
        
        Raises
        ------
        TypeError
            When an element of `newFilters` is not of a TypeFilter object.
        """
        
        # check that all elements in newFilters are TypeFilter objects.
        for filt in newFilters:
            if not isinstance(filt, TypeFilter):
                raise TypeError("filters must be a TypeFilter instance")

        self._filters = list(newFilters)
         
    def filter_targets(self):
        """apply filters to list of targets sequentially
        
        Returns
        -------
        unfilt_targets : list
            list of targets that have not been filtered
            
        """
        unfilt_targets = self.targets
        filt_targets = []
        for filt in self.filters:
            unfilt_targets, filt_tgts = filt(unfilt_targets)
            filt_targets.extend(filt_tgts)
        
        return unfilt_targets

    def run(self):
        """user-defined parser logic.
        """
        raise NotImplementedError()
 
