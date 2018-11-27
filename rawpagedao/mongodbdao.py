from rawpagedao.rawpagedao import RawPageDao
from pymongo import MongoClient

import datetime

class MongoDBDao(RawPageDao):

    '''
    Persists RawPage to MongoDB.
    '''


    def __init__(self, config):

        '''
        Setup an instance of MongoDBDao.
        Keys in config are: host, port, database, collection
        :param config: dict with keys
        '''
        c_copy =  dict(config)
        db = c_copy.pop('db')
        collection = c_copy.pop('collection')

        self.client = MongoClient(**c_copy)
        self.db = self.client[db]
        self.collection = self.db[collection]

    def storePage(self, rawPageData):

        '''
        Stores the given RawPageData object into MongoDB.
        
        Returns None on success, otherwise a string containing
        an error message.
        '''
        isodatetime = rawPageData.datetime.isoformat()
        entry = {
                '_id': f"{rawPageData.url};{isodatetime}",
                'url': rawPageData.url,
                'datetime': isodatetime,
                'statuscode': rawPageData.statuscode,
                'header': rawPageData.header,
                'body': rawPageData.body,
        }
        self.collection.insert_one(entry)

        self.collection.update_one(
                filter={'_id': rawPageData.url},
                update={'$set': { 'last': isodatetime } },
                upsert=True
        )

        print(f"New RawPageData from {rawPageData.url} written")

        return None
