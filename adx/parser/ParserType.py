'''
Class definition of ParserType which holds all the good stuff
'''


class ParserType:
    '''
    
    '''
    def __init__(self):
        '''
        
        Parameters
        ----------
        This class doesn't take any arguments

        Note
        ---
        This class will be heavy
        '''
        # Schema stuff
        self.__schema = []
        self.__StatTrack = 0
        self.__funcs = []
        # Regex Rule stuff
        self.__regrule = None 
        # Signature stuff
        self.__signature = None
        self.__signature__begin = False
        self.__signature__end = False
        # Reader stuff
        self.__reader = None

    def AddExtensionRule(self, extension):
        '''
        Method to add an extension rule.

        Parameter
        --------
        extension : str
            Extension of the files to be trapped. 
        '''
        self.__extensions.append(ex)

    def AddFilenameRule(self, filename):
        '''
        Method to add filename rule.

        Parameters
        ----------

        filename : str
            Part of the filename to check for while trapping
        '''
        self.__filename.append(filename)

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
        self.__regrule = regexp

    def __CreateRegex(self):
        '''
        Private method to create ultimate regex rule which will be passed to Parser.

        Note
        ----
        This method is not exposed to user. It will be internally called. 
        '''

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
        else if signature[0] == '$': 
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
        self.__reader = readme

    def AddFloat(description, func):
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
        self.__schema.append( ('description', 'float')  )
        self.__funcs.append( func  )
        self.__StatTrack = self.__StatTrack + 1 # incrementing counter

    def AddString(description, length, func):
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
        self.__schema.append( ( description, ''.join ( ('string', str(length) ) ) ) )
        self.__funcs.append( func  )
        self.__StatTrack = self.__StatTrack + 1 # incrementing counter

    def __str__(self):
        '''
        So that we can pretty print ParserType objects 
        '''
        # TODO

    def AddOnFile(self, func):
        '''
        Method to bind a function call action on every file which is parsed.

        Parameters
        ----------
        func : Function or callable class 
            IMP func should either take a `reader` class or `filename` as argument

        Note
        ----
        This seems so useful rn.
        '''
        self.__onfilefunc = func





























            
