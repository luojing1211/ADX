'''
So, you thought making an adx class would be illegal. 
Mind 100. Speech 100. Shittttttttttt justttttt gotttt reaaalllll.
Mind=Blown
'''
# local stuff
from parser import Parser
from crawler import Crawler
import mongodbio
import tabio
# other stuff
import multiprocessing as mp

__all__ = ['Adx']

class Adx(object):
    def __init__(self, cdir, pars, 
            logg = 'mongodb', 
            name = 'ttt',
            daemon=True, 
            verbose=0, 
            numthreads=1,
            debug=False):
        '''
        Why even expose Parser class out?
        Make Adx take variable inputs of ParserType instances
        and include them inside. 

        We are just exposing one class that way. Rest is taken care inside and internally.
        
        Signatures not implemented. 
        '''
        # crawl setup
        self.crawler = Crawler(cdir)
        # parse setup
        self.parsers = pars
        # logger setup
        self.logtype = logg
        if logg == 'mongodb':
            self.logger = mongodbio.dbio(dbname = name)
        elif logg == 'tab':
            self.logger = tabio()
        else:
            raise ValueError("Logger type not understood.")
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

