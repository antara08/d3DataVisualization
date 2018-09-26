import json
from pymongo import MongoClient

client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
class read:
    @classmethod
    def readDays(self):
        for x in db.appConfig.find({'key': 'day_365'}, {"key": 1, "value": 1, "_id": 0}):  # 1
            l = x[ 'value' ]
        return l