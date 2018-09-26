import json,os
from pymongo import MongoClient
from datetime import *
import slider as s

client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']

class transferFunction:

 def createData(self,a,b):
  list = [ ]

  d = datetime.now()
  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  for x in db.Transfer_Tables_UTA_Dest.find({"dst_site":a,"src_cloud":b,"to_date":{"$gte": utc_dt_365}},
                                         {"dst_site": 1, "src_cloud": 1,"errors_xs":1,"files_xs":1,"bytes_xs":1,"to_date":1, "_id": 0}):  # 1
    items = {
        'y': x[ "bytes_xs" ],
        'x': str(x[ "to_date" ])
    }
    list.append(items)

  l = json.dumps(list, indent=4, sort_keys=False, encoding='utf-8')
  return l
 def createData1(self,a,b):
  files = [ ]

  d = datetime.now()
  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  for x in db.Transfer_Tables_UTA_Dest.find({"dst_site":a,"src_cloud":b,"to_date":{"$gte": utc_dt_365}},
                                         {"dst_site": 1, "src_cloud": 1,"errors_xs":1,"files_xs":1,"bytes_xs":1,"error_prcnt":1,"to_date":1, "_id": 0}):  # 1
    file={
        'y':x["files_xs"],
        'x':str(x["to_date"])
    }
    files.append(file)

  m = json.dumps(files, indent=4, sort_keys=False, encoding='utf-8')
  return m

 def createData3(self,a,b):
  failure = [ ]

  d = datetime.now()
  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  for x in db.Transfer_Tables_UTA_Dest.find({"dst_site":a,"src_cloud":b,"to_date":{"$gte": utc_dt_365}},
                                         {"dst_site": 1, "src_cloud": 1,"errors_xs":1,"files_xs":1,"bytes_xs":1,"error_prcnt":1,"to_date":1, "_id": 0}):  # 1
    fail={
        'y':x["errors_xs"],
        'x':str(x["to_date"])
    }
    failure.append(fail)

  n = json.dumps(failure, indent=4, sort_keys=False, encoding='utf-8')
  return n

 def createData4(self,a,b):
  prcntage = [ ]

  d = datetime.now()
  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  for x in db.Transfer_Tables_UTA_Dest.find({"dst_site":a,"src_cloud":b,"to_date":{"$gte": utc_dt_365}},
                                         {"dst_site": 1, "src_cloud": 1,"errors_xs":1,"files_xs":1,"bytes_xs":1,"error_prcnt":1,"to_date":1, "_id": 0}):  # 1
    prcnt={
        'y':x["error_prcnt"],
        'x':str(x["to_date"])
    }
    prcntage.append(prcnt)

  o = json.dumps(prcntage, indent=4, sort_keys=False, encoding='utf-8')
  return o