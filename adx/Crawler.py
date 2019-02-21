'''
Crawler class definition
'''

class Crawler:
    '''
    Crawler class
    '''
    def __init__(self):
        # TODO

    def __receive_rules(self, rules):
        '''
        Private method which gets rules from Parser objects.

        Parameters
        ----------

        rules : regex?

        Note
        ----

        You shouldn't probably call this on your own unless you know what you're doing.
        '''
        # TODO 

    def __action(self, filepath):
        '''
        Single atomic action resolution for a filepath

        Parameters
        ----------

        filepath : str
            Filepath
        '''
        # TODO file resolution using rules
        # TODO return PtIndex

    def DoYourThing(self, path):
        '''
        Method which will do the actual crawling

        Parameters
        ----------

        path : str
            directory root from where to start the crawling/tracking/indexing

        Note
        ----

        We might want to change the function names to make them more serious.
        '''
        # TODO
        # TODO should probably call __action 
