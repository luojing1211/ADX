'''
Main Parser class implementation where all the ParserType stuff is injected into
'''


__all__ = ['Parser','ParserType']

import re

class Parser:
    '''
    ain't nobody got time to write the doc string

    Attributes
    ----------

    __rule : list
        List of callables which return bool 
    __parsertype : list
        List of identifiers of parsertype. 
        Identifiers need to be unique.
        Elements of this list are used as keys everywhere.
    __schema : dict
        Dictionary with keys as __parsertype and 
        values as schema requested
    __actions: dict
        Dictionary with keys as __parsertype and 
        values as callable which returns scalar or list 
        depending on the __schema
    __reader: dict
        If any class interface was given, it's loaded

    Assertions
    ----------
    __rule <1-1>  __parsertype
        One to one mapping
    __schema.keys() == __actions.keys() <== keys from __parsertype
    '''

    def __init__(self):
        '''
        Sets up environment
        '''
        self.__rule  = list()
        self.__parsertypes = list()
        self.__actions = dict() # 1-1 on parsertypes
        self.__schema = dict()
        self.__reader = dict() 
        self.__dtypes = dict()

    def __SchemaToLogger(self):
        '''
        Method to get schema as received by the Parser to our brother Logger
        
        Do we actually need it?
        > In db case, we need it to indexing purposes
        > In tab case, we NEED NEED it. 
        Note
        ----

        Tis be a private method. Thou shallnt call thine.
        '''
        # YOLO -- delegating work to future Surya
        return self.__schema

    def parseAction(self, filelist):
        '''
        Method which does the work. 
        Our brother Crawler isn't helping us so it is upto Parser to decide what to do with the file in hand.

        Parameters
        ----------

        filelist : list, or iterable
            List of files

        Returns 
        ------
        ret : dict
        '''
        ret = {ipt:[] for ipt in self.__parsertypes}
        # TODO irule matching
        # TODO signature matching
        # TODO statistics extraction
        # TODO Return stats to Logger
        for fl in filelist:
            k,v = self.__parser(fl)
            if k is None:
                continue
            ret[k].append(v)
        return ret

    def __parser(self, filepath):
        '''
        Method which does the work. 
        Our brother Crawler is helping us by telling us PtIndex.
        PtIndex is index of the ParserType which matches the file at hand.

        Parameters
        ----------

        filepath : str
            The entire filepath

        Note
        ----
        Our brother Crawler might make mistake (but, he's our brother afterall), so if we get ADXMisMatchError anywhere, we fall back to ParserType resolution.
        Do we????
        '''
        for ipt,rulz in zip(self.__parsertypes, self.__rule):
            if rulz(filepath):
                if self.__reader[ipt] is not None:
                    # this ensures that file is read ONLY once
                    fre = self.__reader[ipt]( filepath  )
                else:
                    fre = filepath
                return ipt, {sch:act(fre) for sch,act in zip(self.__schema[ipt],self.__actions[ipt])}
            # This above line is beautiful
        return None, None

    def AddParserType(self, pt):
        '''
        Only method exposed to the user for injection.

        Parameters
        ----------
        pt : ParserType object
            An instance of a ParserType object which contains all the rules.

        Note
        ----
        This is like the wedding of ParserType into Parser.
        '''
        ## yo mama gonna get hitched
        # name
        self.__parsertypes.append( pt.name )
        # rule
        self.__rule.append( pt.rule  )
        # schema
        self.__schema[pt.name] = pt.schema
        # action
        self.__actions[pt.name] = pt.funcs
        # dtype
        self.__dtypes[pt.name] = pt.dtypes
        # reader
        self.__reader[pt.name] = pt.reader

class ParserType:
    '''
    yo mama class    
    '''
    def __init__(self, name):
        '''
        
        Parameters
        ----------
        
        name : str
            Should be fooking unique, dawwwg

        Note
        ---
        This class will be heavy
        '''
        self.name = name # name identifier, should be fooking unique
        # extension
        self.__extension = ''
        # filename
        self.__filename = ''
        # Signature stuff
        self.__signature = None
        self.__signature__begin = False
        self.__signature__end = False
        # wedding stuff
        self.rule = None     # callable biatch
        self.schema = []   # holds the schemas
        self.funcs = []    # holds the semantic action
        self.dtypes = []   # holds the return types 
        self.reader = None # do you even optimize bro?

    def AddExtensionRule(self, extension):
        '''
        Method to add an extension rule.

        Parameter
        --------
        extension : str
            Extension of the files to be trapped. 
        '''
        self.__extension = extension
        self.__CreateRegex()

    def AddFilenameRule(self, filename):
        '''
        Method to add filename rule.

        Parameters
        ----------

        filename : str
            Part of the filename to check for while trapping
        '''
        self.__filename = filename
        self.__CreateRegex()

    def AddFilenameRegexRule(self, regexp):
        '''
        Method to add regex rule for filename based trapping

        Parameters
        ----------
        regexp : str
            Regular expression which should be compiled successfully using Python re module

        Note
        ----
        `ParserType` will not generate a regex rule if the user provides this.
        '''
        try:
            rex = re.compile(regexp)
        except re.error:
            raise ValueError('cannot prepare regex')
        self.rule = lambda x : rex.match(x) is not None

    def __CreateRegex(self):
        '''
        Private method to create ultimate regex rule which will be passed to Parser.

        Will be called after AddExtensionRule, AddFilenameRule, AddFilenameRegexRule
        Note
        ----
        This method is not exposed to user. It will be internally called. 
        '''
        rrule = '$.*' + self.__filename + '.*.' + self.__extension + '$'
        try:
            rex = re.compile(rrule)
        except re.error:
            raise ValueError('Cannot make regex rule')
        self.rule = lambda x : rex.match(x) is not None

    def AddSignature(self, signature):
        '''
        Method to add a signature check.

        Parameters
        ----------

        signature : str
            Signature which will be used to check file

        Note
        ----
        There are some special characters that can be used in defining signature:
            - If the signature begins with '^' (caret) followed by text, the first few lines of the text is read and checked against the text to verify the signature.
            - If the signature ends with '$' (dollar sign), the file under question is checked if it ends with the text preceeding '$'. 

        For example,
            - '^BBX' means file is passed ONLY if the first three characters read from the top of the file match 'BBX'
            - 'XBB$' means file is passed ONLY if the last three characters read from the end of the file match 'XBB'
        '''
        if signature[0] == '^':
            self.__signature__begin = True
            self.__signature__end = False
        elif signature[0] == '$': 
            self.__signature__begin = False 
            self.__signature__end = True 
        self.__signature = signature

    def Reader(self, readme):
        '''
        Method to bind an interface class to interact with the files.

        Parameters
        ----------

        readme : Function or Callable class
            
        Note
        ----

        Define your interface class in the same place where you're defining your ParserType classes
        '''
        self.reader = readme

    def AddPar(self, description, func, dtype='float', length=None):
        '''
        Why have two functions when one function can do the job?
        '''
        self.dtypes.append( dtype if length else dtype+str(length) )
        self.schema.append( description  )
        self.funcs.append( func )

    def AddFloat(self, description, func):
        '''
        Method to add a statistics to be tracked by ADX.

        Parameters
        ----------

        description : str
            A short string which will be used as a column name in database or AstroPy Tables

        func : Function or callable class 
            IMP func should either take a `reader` class or `filename` as argument

        Note
        ----

        Make your life easier by adding a reader class to your `ParserType` instantiation and defining your `func` to take a reader class object as argument.
        '''
        self.dtypes.append( 'float' )
        self.schema.append( description  )
        self.funcs.append( func )

    def AddString(self, description, length, func):
        '''
        Method to add a string based statistics to be tracked by ADX

        Parameters
        ----------

        description : str
            A short string which will be used as a column name in database or AstroPy Tables

        length : int
            Maximum length of the string. 

        func : Function or callable class 
            IMP func should either take a `reader` class or `filename` as argument
        '''
        self.dtypes.append( 'string'+str(length) )
        self.schema.append( description )
        self.funcs.append( func  )

    def AddOnFile(self, func):
        '''
        Method to bind a function call action on every file which is parsed.

        Parameters
        ----------
        func : Function or callable class 
            IMP func should either take a `reader` class or `filename` as argument

        Note
        ----
        This seems so useful rn. F this shit. 
        Now, I don't know it felt so important then.
        '''
        self.__onfilefunc = func

    def AddDirectoryRule(self):
        # TODO
        pass
