'''
Main Parser class implementation where all the ParserType stuff is injected into
'''


__all__ = ['Parser']


class Parser:
    '''
    ain't nobody got time to write the doc string
    '''
    def __init__(self, *args, **kwargs):
        # TODO 
        self.__rule  = None

    def __RulesToCrawler(self):
        '''
        Method to get rules to crawler so that it can do the filetype resolution for us.

        Note
        ----

        Tis be a private method. Thou shallnt call thine.
        '''
        # TODO

    def __SchemaToLogger(self):
        '''
        Method to get schema as received by the Parser to our brother Logger

        Note
        ----

        Tis be a private method. Thou shallnt call thine.
        '''
        # YOLO
        # TODO

    def __call__(self, filepath):
        '''
        Method which does the work. 
        Our brother Crawler isn't helping us so it is upto Parser to decide what to do with the file in hand.

        Parameters
        ----------

        filepath : str
            The entire filepath
        '''
        try:
            for idx, irule in enumerate(self.__rule) :
                # TODO irule matching
                # TODO signature matching
                # TODO statistics extraction
                # TODO Return stats to Logger
        except ADXReadError:
            raise ADXReadFail

    def __call__(self, filepath, PtIndex):
        '''
        Method which does the work. 
        Our brother Crawler is helping us by telling us PtIndex.
        PtIndex is index of the ParserType which matches the file at hand.

        Parameters
        ----------

        filepath : str
            The entire filepath

        PtIndex : int
            Index of the ParserType object which is resolved by our brother Crawler

        Note
        ----
        Our brother Crawler might make mistake (but, he's our brother afterall), so if we get ADXMisMatchError anywhere, we fall back to ParserType resolution.
        '''
        try:
            # TODO irule matching
            # TODO signature matching
            # TODO statistics extraction
            # TODO Return stats to Logger
        except ADXMismatchError:
            self.__call__(filepath)


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
        
        # inject regex rule
        if pt.__regrule is None:
            self.__rule.append( pt.__CreateRegex() )
        elif:
            self.__rule.append( pt.__regrule )

        # inject schema
        if not pt.__StatTrack:
            self.__schema.append( pt.__schema  )
        else:
            self.__schema.append( [] )

        # inject funcs
        # TODO

        # inject reader
        # TODO

        # inject signature
        # TODO

        # inject TODO




















