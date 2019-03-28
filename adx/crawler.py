'''
Crawler class definition
'''
import os

class Crawler:
    '''
    Crawler class


    N.B. Delegate all multi threading to ADX class
    as multi-threading in CPython negatively affects performance due to
    Global Interpreter Lock.
    Make use of multiprocessing.
    '''
    def __init__(self, 
            cdir,
            followLinks = False,
            ):
        self.workd = []
        if isinstance(cdir, str):
            cdir = [ cdir ]
        self.workd = self.workd + cdir
        self.flinks = followLinks

    def __iter__(self):
        # yield a tuple dawg
        for cd in self.workd:
            for dirpath, dirs, files in  os.walk(cd, followlinks = self.flinks):
                yield dirpath, files

