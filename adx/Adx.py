'''
ADX main class definition
'''
# ADX stuff
from parser import Parser
from crawler import Crawler
# other stuff
import multiprocessing as mp

__all__ = ['Adx']

class Adx(object):
    def __init__(self, cdir, pars, logg,
            daemon=True, 
            verbose=0, 
            numthreads=1,
            debug=False):
        '''
        Arguments
        ---------

        cdir : str, or list of str
            Directory or list of directories to crawl
        pars : instance of Parser or list of ParserTypes
        logg : any instance of logging

        '''
        # crawl setup
        self.crawler = Crawler(cdir)
        # parse setup
        if isinstance(Parser, pars):
            self.parsers = pars
        elif isinstance(list, pars):
            self.parsers = Parser()
            for pt in pars:
                self.parsers.AddParserType(pt)
        # logger setup
        self.logger = logg
        # misc options
        self.daemon = daemon
        self.debug = debug
        self.verbose = 3 if debug else verbose
        self.numthreads = numthreads if numthreads < mp.cpu_count() else mp.cpu_count()
        # max number of threads is number of CPUs

    def __step(self,currdir, curr):
        # moving mountains
        # one rock at a time
        # to ensure grouped and make use of InsertMany
        rdict =  self.parsers.parseAction(curr)
        for k,v in rdict.items():
            if len(v) == 0:
                continue
            self.logger.InsertMany(k,v)

    def __setup(self):
        # this isn't necessary anymore 
        # self.logger.getSchema( self.parser.putSchema() )
        pass

    def walk(self):
        for pdir, curr in self.crawler:
            self.__step(pdir, curr)

