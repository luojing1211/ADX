'''Handles db io'''

# Are we using NoSQL? 
# MySQL?
# MongoDB?
# Why are bothering about schema?? 
# I feel so dumb at times. 

'''
MongoDB --> single db.
MongoDB --> every collection corresponds to a particular parserType 
Although no schema is enforced in MongoDB, instead of doing blind collection scan everytime, 
it be better to have indexing whenever so that querying can be optimized. 
Schema is therefore not enforced.
'''

import pymongo as pmdb

class dbio(pmdb.MongoClient):
    def __init__(self,
            name = 'localhost:84001',
            dbname = 'name'
            ):
        ip, port = name.split(':')
        super(dbio, self).__init__(name)
        self.db = self[dbname]
        self.ptypes = self.db.list_collection_names()
        self.schema = {ix:[] for ix in self.ptypes}
        # TODO

    def __getitem__(self, key):
        # XXX Is this proper? To have exception in conditionals
        if key not in self.ptypes:
            raise KeyError("ParserType key not found.")
        return self.db[key]

    def __feedSchema__(self, schema):
        # schema be a dict. 
        # each key is pt
        # each value is iterable
        for k,v in schema.iteritems():
            if k in self.ptypes:
                # ptypes was initialized before?
                # okay..
                self.schema[k] = self.schema[k] + v
            else:
                self.ptypes.append(k)
                self.schema[k] = v
        assert set(self.schema.keys()) == set( self.ptypes )
        # we anyway shouldn't have any duplicates smh


    def Query(self, qpt, query):
        # need to decide on the grammar
        # TODO it be fun to implement this
        return self[qpt].find(query)

    def InsertOne(self, qpt, payload):
        return self[qpt].insert_one(payload)

    def InsertMany(self, qpt, payload):
        return self[qpt].insert_many(payload)

    def DeleteOne(self, qpt, pred):

    def Close(self):
        # CLOSE DB
        self.close()



