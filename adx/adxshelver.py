'''
Shelving class
'''
import shelve as sh

class Shelver():
    '''
    Manages the shelving actions
    '''
    def __init__(self, filename):
        self.shelf = sh.open(filename)
        self.filename = filename

    def close(self):
        self.shelf.close()
        # delete file

    def list(self):
        return self.shelf.keys()

    def save(self, k, v):
        self.shelf[k] = v

    def get(self, k):
        return self.shelf[k]

    def savefilename(self,path, session):
        f = open(path + session,'w')
        f.write(self.filename)
        f.close()

