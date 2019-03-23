import subprocess

class dbd:
    def __init__(self, 
            dbpath,  
            bind_ip = 'localhost',
            port = 87654,
            maxc = 5,
            daemon = True,
            logpath = None,
            ):
        # python daemon ????
        # Having a separate class for dbdaemon?
        # check if mongod is already running
        # mongorestore
        # mongodump
        if 
