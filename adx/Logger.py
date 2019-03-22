'''
Logger class definition
'''

from adx.io import dbio
from adx.io import tabio


class Logger:
    '''
    Logger class
    '''
    def __init__(self, name=None, numtables=1, writeDB=None):
        if self.validIP(name):
            # need to write to a db
            self.sqldb = True
            self.log = dbio(ip, port, writeDB)
            if writeDB is None:
                self.writedb = name
            else:
                self.writedb = writeDB
        else:
            # need to write tables
            self.logdir = name

    def __addSchema(self, name, dtype):
        if name in self.schema:
            raise ADXLogError("Schema ill-defined.")
        self.schema.append(name)
        self.schema_dtype.append(dtype)

    def __prepareLog(self):
        self.log()

    def getSchema(self, schema):
        '''
        Private method which gets schema from Parser objects.

        Parameters
        ----------

        schema : list or str
            schema <- 'sn:float'
            schema <- 'backend:str(256)'
            schema <- [ 'sn:float', 'backend:str(256)'  ]

        Note
        ----

        You shouldn't probably call this on your own unless you know what you're doing.
        '''
        if isinstance(schema, list):
            # multiple schemas
            for s in schema:
                par, val = s.split(':')
                self.__addSchema(par, val)
        elif isinstance(schema,str):
            # only one schema
            par, val = schema.split(':')
            self.__addSchema(par, val)
            
    def log(self, pt, ddir, data):
        '''
        Single atomic action resolution for a filepath

        Parameters
        ----------

        data : dict ? 
            which is to be retured by the Parser
        '''
        if pt not in self.schema:
            raise ADXLogError("ParserType not recognized.")
        if self.sqldb:
            self.__writeDB(ddir, data)
            # INSERT INTO ?(pt) VALUES (?,?,?...)
        else self.atables:
            self.__writeTab(ddir, data)
