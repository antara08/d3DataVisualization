import json,os
import pymongo
from pymongo import MongoClient
from datetime import *
import ConfigParser
import slider as s
dirname=os.getcwd()
#dirname = os.path.dirname(__file__)



client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']

Config = ConfigParser.ConfigParser()
filename = dirname + '/config.cfg'
try:
    Config.read(filename)
except Exception as e:
    print(str(e))


class utaswt2:
 rse_all=[]

 rucio_7 = [ ]
 rucio1_7 = [ ]
 expired_7 = [ ]
 expired1_7 = [ ]
 gsiftp_7 = [ ]
 gsiftp1_7 = [ ]
 obsolete_7 = [ ]
 obsolete1_7 = [ ]
 jsonx_7 = [ ]
 jsonx1_7 = [ ]
 unavailable_7 = [ ]
 unavailable1_7 = [ ]

 global d
 d = datetime.now()

 @classmethod
 def data_prep(self):
  rucio = [ ]
  rucio1 = [ ]
  expired = [ ]
  expired1 = [ ]
  gsiftp = [ ]
  gsiftp1 = [ ]
  obsolete = [ ]
  obsolete1 = [ ]
  jsonx = [ ]
  jsonx1 = [ ]
  unavailable = [ ]
  unavailable1 = [ ]
  list1 = [ ]
  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  db.rucio_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
  for x in db.rucio_UTA_SWT2.find({"updated_at": {"$gte": utc_dt_365}}, {"used": 1,"updated_at":1, "_id": 0}):      #1
     items={
           'y': x[ "used" ],
           'x': str(x["updated_at"].strftime('%d-%b-%Y %H:%M:%S')),
           'source':'rucio'
     }
     rucio.append(items)
     list1.append(items)
  db.expired_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
  for x in db.expired_UTA_SWT2.find({"updated_at":{"$gte": utc_dt_365}}, {"used": 1,"updated_at":1, "_id": 0}):        #2
       items={
           'y': x[ "used" ],
           'x' : str(x["updated_at"]),
           'source':'expired'
       }
       expired.append(items)
       list1.append(items)
  db.gsiftp_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
  for x in db.gsiftp_UTA_SWT2.find({"updated_at":{"$gte": utc_dt_365}}, {"used": 1,"updated_at":1, "_id": 0}):     #3
       items={
           'y': x[ "used" ],
           'x' : str(x["updated_at"]),
           'source': 'gsiftp'
       }
       gsiftp.append(items)
       list1.append(items)
  db.obsolete_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
  for x in db.obsolete_UTA_SWT2.find({"updated_at":{"$gte": utc_dt_365}}, {"used": 1,"updated_at":1, "_id": 0}):       #5
       items={
           'y': x[ "used" ],
           'x' : str(x["updated_at"]),
           'source': 'obsolete'
       }
       obsolete.append(items)
       list1.append(items)
  db.json_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
  for x in db.json_UTA_SWT2.find({"updated_at": {"$gte": utc_dt_365}}, {"used": 1,"updated_at":1, "_id": 0}):       #6
       items={
           'y': x[ "used" ],
           'x' : str(x["updated_at"]),
           'source': 'json'
       }
       jsonx.append(items)
       list1.append(items)
  db.unavailable_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
  for x in db.unavailable_UTA_SWT2.find({"updated_at":{"$gte": utc_dt_365}}, {"used": 1,"updated_at":1, "_id": 0}):            #9
       items={
           'y': x[ "used" ],
           'x' : str(x["updated_at"]),
           'source': 'unavailable'
       }
       unavailable.append(items)
       list1.append(items)

  json_list=json.dumps(list1,indent=4,sort_keys=False,encoding='utf-8') #data for the multi-line chart

  if (len(rucio1) != 0):   #1
       rucio1=[]
       rucio1 = rucio
       rucio=[]
  else:
       rucio1 = rucio
       rucio=[]
  if(len(expired1)!=0):     #2
      expired1=[]
      expired1 = expired
      expired = [ ]
  else:
      expired1=expired
      expired=[]
  if (len(gsiftp1) != 0):       #3
       gsiftp1=[]
       gsiftp1 = gsiftp
       gsiftp = [ ]
  else:
       gsiftp1 = gsiftp
       gsiftp=[]
  if (len(obsolete1) != 0):     #5
       obsolete1=[]
       obsolete1 = obsolete
       obsolete = [ ]
  else:
       obsolete1 = obsolete
       obsolete=[]
  if (len(jsonx1) != 0):     #6
           jsonx1=[]
           jsonx1 = jsonx
           jsonx = [ ]
  else:
           jsonx1 = jsonx
           jsonx=[]
  if (len(unavailable1) != 0):      #7
          unavailable1=[]
          unavailable1 = unavailable
          unavailable = [ ]
  else:
          unavailable1 = unavailable
          unavailable=[ ]
  rucio_yr=json.dumps(rucio1, indent=4, sort_keys=False, encoding='utf-8')
  expired_yr=json.dumps(expired1, indent=4, sort_keys=False, encoding='utf-8')
  gsiftp_yr=json.dumps(gsiftp1, indent=4, sort_keys=False, encoding='utf-8')
  obsolete_yr=json.dumps(obsolete1, indent=4, sort_keys=False, encoding='utf-8')
  json_yr=json.dumps(jsonx1, indent=4, sort_keys=False, encoding='utf-8')
  unavailable_yr=json.dumps(unavailable1, indent=4, sort_keys=False, encoding='utf-8')

  return json_list,rucio_yr,expired_yr,gsiftp_yr,obsolete_yr,json_yr,unavailable_yr

#----------------------------------------------------data for last 7 days-----------------------------------------------------
 d = datetime.now()
 delta_7 = Config.getint('swt2_cpb', 'days7')
 utc_dt =d.utcnow() + timedelta(delta_7)

 db.rucio_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
 for x in db.rucio_UTA_SWT2.find({"updated_at": {"$gte": utc_dt}}, {"used": 1,"updated_at":1, "_id": 0}):      #1
      items={
          'y': x[ "used" ],
          'x': str(x["updated_at"].strftime('%d-%b-%Y %H:%M:%S'))
      }
      rucio_7.append(items)
 db.json_UTA_SWT2.find({}).sort("updated_at",pymongo.ASCENDING)
 for x in db.json_UTA_SWT2.find({"updated_at": {"$gte": utc_dt}}, {"used": 1, "updated_at": 1, "_id": 0}):  # 2
     items = {
         'y': x[ "used" ],
         'x': str(x[ "updated_at" ])
     }
     jsonx_7.append(items)
 db.expired_UTA_SWT2.find({}).sort("updated_at",pymongo.ASCENDING)
 for x in db.expired_UTA_SWT2.find({"updated_at": {"$gte": utc_dt}}, {"used": 1,"updated_at":1, "_id": 0}):        #4
      items={
          'y': x[ "used" ],
          'x' : str(x["updated_at"])
      }
      expired_7.append(items)

 db.gsiftp_UTA_SWT2.find({}).sort("updated_at",pymongo.ASCENDING)
 for x in db.gsiftp_UTA_SWT2.find({"updated_at": {"$gte": utc_dt}}, {"used": 1,"updated_at":1, "_id": 0}):     #3
      items={
          'y': x[ "used" ],
          'x' : str(x["updated_at"])
      }
      gsiftp_7.append(items)
 db.obsolete_UTA_SWT2.find({}).sort("updated_at",pymongo.ASCENDING)
 for x in db.obsolete_UTA_SWT2.find({"updated_at": {"$gte": utc_dt}}, {"used": 1,"updated_at":1, "_id": 0}):       #5
      items={
          'y': x[ "used" ],
          'x' : str(x["updated_at"])
      }
      obsolete_7.append(items)
 db.unavailable_UTA_SWT2.find({}).sort("updated_at",pymongo.ASCENDING)
 for x in db.unavailable_UTA_SWT2.find({"updated_at": {"$gte": utc_dt}}, {"used": 1,"updated_at":1, "_id": 0}):            #6
      items={
          'y': x[ "used" ],
          'x' : str(x["updated_at"])
      }
      unavailable_7.append(items)



 if (len(rucio1_7) != 0):   #1
      rucio1_7=[]
      rucio1_7 = rucio_7
      rucio_7=[]
 else:
      rucio1_7 = rucio_7
      rucio_7=[]
 if(len(expired1_7)!=0):     #2
     expired1_7=[]
     expired1_7 = expired_7
     expired_7 = [ ]
 else:
     expired1_7=expired_7
     expired_7=[]
 if (len(gsiftp1_7) != 0):       #3
      gsiftp1_7=[]
      gsiftp1_7 = gsiftp_7
      gsiftp_7 = [ ]
 else:
      gsiftp1_7 = gsiftp_7
      gsiftp_7=[]
 if (len(obsolete1_7) != 0):     #5
          obsolete1_7=[]
          obsolete1_7 = obsolete_7
          obsolete_7 = [ ]
 else:
          obsolete1_7 = obsolete_7
          obsolete_7=[]
 if (len(jsonx1_7) != 0):     #6
          jsonx1_7=[]
          jsonx1_7 = jsonx_7
          jsonx_7 = [ ]
 else:
          jsonx1_7 = jsonx_7
          jsonx_7=[]

 if (len(unavailable1_7) != 0):      #9
          unavailable1_7=[]
          unavailable1_7 = unavailable_7
          unavailable_7 = [ ]
 else:
          unavailable1_7 = unavailable_7
          unavailable_7=[]
 ruciox_7=json.dumps(rucio1_7, indent=4, sort_keys=False, encoding='utf-8')
 expiredx_7=json.dumps(expired1_7, indent=4, sort_keys=False, encoding='utf-8')
 gsiftpx_7 = json.dumps(gsiftp1_7, indent=4, sort_keys=False, encoding='utf-8')
 obsoletex_7 = json.dumps(obsolete1_7, indent=4, sort_keys=False, encoding='utf-8')
 jsonx_7 = json.dumps(jsonx1_7, indent=4, sort_keys=False, encoding='utf-8')
 unavailablex_7 = json.dumps(unavailable1_7, indent=4, sort_keys=False, encoding='utf-8')
