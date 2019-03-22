'''
So, you thought making an adx class would be illegal. 
Mind 100. Speech 100. Shittttttttttt justttttt gotttt reaaalllll.
Mind=Blown
'''

from adx.parser import parser
from adx.crawler import crawler
from adx.logger import logger

class Adx(object):
    def __init__(self, craw, pars, logg, 
            daemon=True, 
            verbose=0, 
            numthreads=1
            debug=False):
        # crawl setup
        if isinstance(craw,crawler):
            self.crawler = [ craw ]
        elif isinstance(craw, list):
            self.crawler = craw
        else:
            raise ADXCrawlError("Crawler passed not understood.")
        # parse setup
        if isinstance(pars,parser):
            self.parsers = [pars]
        elif isinstance(pars, list):
            self.parsers = pars
        else:
            raise ADXCrawlError("Parser not understood.")
        # logger setup
        self.logger = logg
        # misc options
        self.daemon = daemon
        self.debug = debug
        self.verbose = 3 if debug else verbose
        self.numthreads = numthreads if numthreads < mp.cpu_count() else mp.cpu_count()
        # max number of threads is CPU

    def __step(self,currdir, curr):
        # moving mountains
        # one rock at a time
        # `batchsize` number of elements
        pt, parsedCurr = self.parsers.parseAction(curr)
        self.logger.log(pt, currdir, parsedCurr)

    def __setup(self):
        # this isn't necessary anymore 
        # self.logger.getSchema( self.parser.putSchema() )
        # 

    def walk(self):
        for pdir, curr in self.crawler:
            self.__step(pdir, curr)

