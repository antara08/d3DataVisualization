import json,os
import pymongo
from pymongo import MongoClient
from datetime import *
import slider as s
import ConfigParser
#dirname = os.path.dirname(__file__)
dirname =  os.getcwd()



client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
Config = ConfigParser.ConfigParser()
filename = dirname+'/config.cfg'
try:
     Config.read(filename)
except Exception as e:
     print(str(e))

# DDM JSON URL for our sites as a destination AND deletions (LAST HOUR)
class Del:

 key_deletions=[]
 key_deletions1=[]
 row1=[]
 row2=[]
 row3=[]
 planned_bytes_list = []
 planned_bytes_list1=[]
 failed_bytes_list=[]
 failed_bytes_list1=[]
 done_bytes_list=[]
 done_bytes_list1=[]

 planned_files_list = []
 planned_files_list1=[]
 failed_files_list=[]
 failed_files_list1=[]
 done_files_list=[]
 done_files_list1=[]

 planned_bytes_list_uta_swt2 = [ ]
 planned_bytes_list1_uta_swt2 = [ ]
 failed_bytes_list_uta_swt2 = [ ]
 failed_bytes_list1_uta_swt2 = [ ]
 done_bytes_list_uta_swt2 = [ ]
 done_bytes_list1_uta_swt2 = [ ]
 planned_files_list_uta_swt2 = [ ]
 planned_files_list1_uta_swt2 = [ ]
 failed_files_list_uta_swt2 = [ ]
 failed_files_list1_uta_swt2 = [ ]
 done_files_list_uta_swt2 = [ ]
 done_files_list1_uta_swt2 = [ ]

 planned_bytes_list_ou_oscer = [ ]
 planned_bytes_list1_ou_oscer = [ ]
 failed_bytes_list_ou_oscer = [ ]
 failed_bytes_list1_ou_oscer = [ ]
 done_bytes_list_ou_oscer = [ ]
 done_bytes_list1_ou_oscer = [ ]
 planned_files_list_ou_oscer = [ ]
 planned_files_list1_ou_oscer = [ ]
 failed_files_list_ou_oscer = [ ]
 failed_files_list1_ou_oscer = [ ]
 done_files_list_ou_oscer = [ ]
 done_files_list1_ou_oscer = [ ]

 planned_bytes_list_luccile = [ ]
 planned_bytes_list1_luccile = [ ]
 failed_bytes_list_luccile= [ ]
 failed_bytes_list1_luccile= [ ]
 done_bytes_list_luccile= [ ]
 done_bytes_list1_luccile= [ ]
 planned_files_list_luccile = [ ]
 planned_files_list1_luccile = [ ]
 failed_files_list_luccile= [ ]
 failed_files_list1_luccile= [ ]
 done_files_list_luccile= [ ]
 done_files_list1_luccile= [ ]


 planned_bytes_list_yr_luccile= [ ]
 planned_bytes_list1_yr_luccile= [ ]
 failed_bytes_list_yr_luccile= [ ]
 failed_bytes_list1_yr_luccile= [ ]
 done_bytes_list_yr_luccile= [ ]
 done_bytes_list1_yr_luccile= [ ]
 planned_files_list_yr_luccile= [ ]
 planned_files_list1_yr_luccile= [ ]
 failed_files_list_yr_luccile= [ ]
 failed_files_list1_yr_luccile= [ ]
 done_files_list_yr_luccile= [ ]
 done_files_list1_yr_luccile= [ ]
 list_luccile= [ ]

 global d
 d = datetime.now()

 d1 = datetime.now()
 delta_7 = Config.getint('deletion', 'days7')
 d2 = d1.utcnow() + timedelta(delta_7)
########################################################## SWT2_CPB ################################################################
 db.del_SWT2_CPB.find({}).sort("to_date", pymongo.ASCENDING)
 for x in db.del_SWT2_CPB.find({"to_date": {"$gte":d2}}):
       planned_bytes = {
           'y': x[ "planned_bytes_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_bytes_list.append(planned_bytes)
       failed_bytes ={
          'y': x[ "failed_bytes_xs" ],
          'x': str(x[ "to_date" ])

       }
       failed_bytes_list.append(failed_bytes)
       done_bytes={
          'y':x["done_bytes_xs"],
          'x':str(x["to_date"])
       }
       done_bytes_list.append(done_bytes)
       planned_files = {
     'y': x[ "planned_files_xs" ],
     'x': str(x[ "to_date" ])
      }
       planned_files_list.append(planned_files)
       failed_files = {
     'y': x[ "failed_files_xs" ],
     'x': str(x[ "to_date" ])
      }
       failed_files_list.append(failed_files)
       done_files = {
     'y': x[ "done_files_xs" ],
     'x': str(x[ "to_date" ])
      }
       done_files_list.append(done_files)
 if (planned_bytes_list):
      planned_bytes_list1 = planned_bytes_list
      planned_bytes_list = [ ]
 if (failed_bytes_list):
      failed_bytes_list1 = failed_bytes_list
      failed_bytes_list = [ ]
 if (done_bytes_list):
      done_bytes_list1 = done_bytes_list
      done_bytes_list = [ ]
 if (planned_files_list):
     planned_files_list1 = planned_files_list
     planned_files_list = [ ]
 if (failed_files_list):
     failed_files_list1 = failed_files_list
     failed_files_list = [ ]
 if (done_files_list):
     done_files_list1 = done_files_list
     done_files_list = [ ]

 planned_bytes_swt2_cpb = json.dumps(planned_bytes_list1, indent=4, sort_keys=False, encoding='utf-8')
 failed_bytes_swt2_cpb = json.dumps(failed_bytes_list1, indent=4, sort_keys=False, encoding='utf-8')
 done_bytes_swt2_cpb = json.dumps(done_bytes_list1, indent=4, sort_keys=False, encoding='utf-8')
 planned_files_swt2_cpb = json.dumps(planned_files_list1, indent=4, sort_keys=False, encoding='utf-8')
 failed_files_swt2_cpb = json.dumps(failed_files_list1, indent=4, sort_keys=False, encoding='utf-8')
 done_files_swt2_cpb = json.dumps(done_files_list1, indent=4, sort_keys=False, encoding='utf-8')
 # --------------------------------------------------------------------------------
 @classmethod
 def data_prep_swt2_cpb(self):
  planned_bytes_list_yr_swt2_cpb = [ ]
  planned_bytes_list1_yr_swt2_cpb = [ ]
  failed_bytes_list_yr_swt2_cpb = [ ]
  failed_bytes_list1_yr_swt2_cpb = [ ]
  done_bytes_list_yr_swt2_cpb = [ ]
  done_bytes_list1_yr_swt2_cpb = [ ]
  planned_files_list_yr_swt2_cpb = [ ]
  planned_files_list1_yr_swt2_cpb = [ ]
  failed_files_list_yr_swt2_cpb = [ ]
  failed_files_list1_yr_swt2_cpb = [ ]
  done_files_list_yr_swt2_cpb = [ ]
  done_files_list1_yr_swt2_cpb = [ ]
  list_swt2_cpb = [ ]

  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))
  db.del_SWT2_CPB.find({}).sort("to_date", pymongo.ASCENDING)
  for x in db.del_SWT2_CPB.find({"to_date": {"$gt": utc_dt_365}}):
        planned_bytes = {
            'y': x[ "planned_bytes_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_bytes'
        }
        planned_bytes_list_yr_swt2_cpb.append(planned_bytes)
        failed_bytes ={
           'y': x[ "failed_bytes_xs" ],
           'x': str(x[ "to_date" ]),
           'source': 'failed_bytes'
        }
        failed_bytes_list_yr_swt2_cpb.append(failed_bytes)
        done_bytes={
           'y':x["done_bytes_xs"],
           'x':str(x["to_date"]),
           'source':'done_bytes'
        }
        done_bytes_list_yr_swt2_cpb.append(done_bytes)
        planned_files = {
            'y': x[ "planned_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_files'
        }
        planned_files_list_yr_swt2_cpb.append(planned_files)
        list_swt2_cpb.append(planned_files)
        failed_files = {
            'y': x[ "failed_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'failed_files'
        }
        failed_files_list_yr_swt2_cpb.append(failed_files)
        list_swt2_cpb.append(failed_files)
        done_files = {
            'y': x[ "done_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'done_files'
        }
        done_files_list_yr_swt2_cpb.append(done_files)
        list_swt2_cpb.append(done_files)



  if(planned_bytes_list_yr_swt2_cpb):
      planned_bytes_list1_yr_swt2_cpb=planned_bytes_list_yr_swt2_cpb
      planned_bytes_list_yr_swt2_cpb=[]
  if (failed_bytes_list_yr_swt2_cpb):
      failed_bytes_list1_yr_swt2_cpb = failed_bytes_list_yr_swt2_cpb
      failed_bytes_list_yr_swt2_cpb = [ ]
  if (done_bytes_list_yr_swt2_cpb):
      done_bytes_list1_yr_swt2_cpb = done_bytes_list_yr_swt2_cpb
      done_bytes_list_yr_swt2_cpb = [ ]
  if(planned_files_list_yr_swt2_cpb):
      planned_files_list1_yr_swt2_cpb=planned_files_list_yr_swt2_cpb
      planned_files_list_yr_swt2_cpb=[]
  if (failed_files_list_yr_swt2_cpb):
      failed_files_list1_yr_swt2_cpb = failed_files_list_yr_swt2_cpb
      failed_files_list_yr_swt2_cpb = [ ]
  if (done_files_list_yr_swt2_cpb):
      done_files_list1_yr_swt2_cpb = done_files_list_yr_swt2_cpb
      done_files_list_yr_swt2_cpb = [ ]


  planned_bytes_yr_swt2_cpb=json.dumps(planned_bytes_list1_yr_swt2_cpb, indent=4, sort_keys=False, encoding='utf-8')
  failed_bytes_yr_swt2_cpb=json.dumps(failed_bytes_list1_yr_swt2_cpb,indent=4, sort_keys =False, encoding='utf-8')
  done_bytes_yr_swt2_cpb=json.dumps(done_bytes_list1_yr_swt2_cpb,indent=4, sort_keys =False, encoding='utf-8')
  planned_files_yr_swt2_cpb = json.dumps(planned_files_list1_yr_swt2_cpb, indent=4, sort_keys=False, encoding='utf-8')
  failed_files_yr_swt2_cpb = json.dumps(failed_files_list1_yr_swt2_cpb, indent=4, sort_keys=False, encoding='utf-8')
  done_files_yr_swt2_cpb = json.dumps(done_files_list1_yr_swt2_cpb, indent=4, sort_keys=False, encoding='utf-8')
  list_swt2_cpb=json.dumps(list_swt2_cpb,indent=4, sort_keys =False, encoding='utf-8')

  return list_swt2_cpb,planned_bytes_yr_swt2_cpb,failed_bytes_yr_swt2_cpb,done_bytes_yr_swt2_cpb,planned_files_yr_swt2_cpb,failed_files_yr_swt2_cpb,done_files_yr_swt2_cpb


########################################################## UTA_SWT2 ################################################################
 db.del_UTA_SWT2.find({}).sort("to_date", pymongo.ASCENDING)
 for x in db.del_UTA_SWT2.find({"to_date": {"$gte":d2}}):
       planned_bytes = {
           'y': x[ "planned_bytes_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_bytes_list_uta_swt2.append(planned_bytes)
       failed_bytes ={
          'y': x[ "failed_bytes_xs" ],
          'x': str(x[ "to_date" ])

       }
       failed_bytes_list_uta_swt2.append(failed_bytes)
       done_bytes={
          'y':x["done_bytes_xs"],
          'x':str(x["to_date"])
       }
       done_bytes_list_uta_swt2.append(done_bytes)
       planned_files = {
           'y': x[ "planned_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_files_list.append(planned_files)
       failed_files = {
           'y': x[ "failed_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       failed_files_list.append(failed_files)
       done_files = {
           'y': x[ "done_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       done_files_list.append(done_files)
 if (planned_bytes_list_uta_swt2):
      planned_bytes_list1_uta_swt2 = planned_bytes_list_uta_swt2
      planned_bytes_list_uta_swt2 = [ ]
 if (failed_bytes_list_uta_swt2):
      failed_bytes_list1_uta_swt2 = failed_bytes_list_uta_swt2
      failed_bytes_list_uta_swt2 = [ ]
 if (done_bytes_list_uta_swt2):
     done_bytes_list1_uta_swt2 = done_bytes_list_uta_swt2
     done_bytes_list_uta_swt2 = [ ]
 if (planned_files_list):
     planned_files_list1_uta_swt2 = planned_files_list
     planned_files_list = [ ]
 if (failed_files_list):
     failed_files_list1_uta_swt2 = failed_files_list
     failed_files_list = [ ]
 if (done_files_list):
     done_files_list1_uta_swt2 = done_files_list
     done_files_list = [ ]

 planned_bytes_uta_swt2 = json.dumps(planned_bytes_list1_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
 failed_bytes_uta_swt2 = json.dumps(failed_bytes_list1_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
 done_bytes_uta_swt2 = json.dumps(done_bytes_list1_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
 planned_files_uta_swt2 = json.dumps(planned_files_list1_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
 failed_files_uta_swt2 = json.dumps(failed_files_list1_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
 done_files_uta_swt2 = json.dumps(done_files_list1_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
 # --------------------------------------------------------------------------------
 @classmethod
 def data_prep_uta_swt2(self):
  planned_bytes_list_yr_uta_swt2 = [ ]
  planned_bytes_list1_yr_uta_swt2 = [ ]
  failed_bytes_list_yr_uta_swt2 = [ ]
  failed_bytes_list1_yr_uta_swt2 = [ ]
  done_bytes_list_yr_uta_swt2 = [ ]
  done_bytes_list1_yr_uta_swt2 = [ ]
  planned_files_list_yr_uta_swt2 = [ ]
  planned_files_list1_yr_uta_swt2 = [ ]
  failed_files_list_yr_uta_swt2 = [ ]
  failed_files_list1_yr_uta_swt2 = [ ]
  done_files_list_yr_uta_swt2 = [ ]
  done_files_list1_yr_uta_swt2 = [ ]
  list_uta_swt2 = [ ]

  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  db.del_UTA_SWT2.find({}).sort("to_date", pymongo.ASCENDING)
  for x in db.del_UTA_SWT2.find({"to_date": {"$gt": utc_dt_365}}):
        planned_bytes = {
            'y': x[ "planned_bytes_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_bytes'
        }
        planned_bytes_list_yr_uta_swt2.append(planned_bytes)
        failed_bytes ={
           'y': x[ "failed_bytes_xs" ],
           'x': str(x[ "to_date" ]),
           'source': 'failed_bytes'
        }
        failed_bytes_list_yr_uta_swt2.append(failed_bytes)
        done_bytes={
           'y':x["done_bytes_xs"],
           'x':str(x["to_date"]),
           'source':'done_bytes'
        }
        done_bytes_list_yr_uta_swt2.append(done_bytes)
        planned_files = {
            'y': x["planned_files_xs"],
            'x': str(x["to_date"]),
            'source':'planned_files'
        }
        planned_files_list_yr_uta_swt2.append(planned_files)
        list_uta_swt2.append(planned_files)
        failed_files = {
            'y': x["failed_files_xs"],
            'x': str(x["to_date"]),
            'source': 'failed_files'
        }
        failed_files_list_yr_uta_swt2.append(failed_files)
        list_uta_swt2.append(failed_files)
        done_files = {
            'y': x["done_files_xs"],
            'x': str(x["to_date"]),
            'source': 'done_files'
        }
        done_files_list_yr_uta_swt2.append(done_files)
        list_uta_swt2.append(done_files)


  if(planned_bytes_list_yr_uta_swt2):
      planned_bytes_list1_yr_uta_swt2=planned_bytes_list_yr_uta_swt2
      planned_bytes_list_yr_uta_swt2=[]
  if (failed_bytes_list_yr_uta_swt2):
      failed_bytes_list1_yr_uta_swt2 = failed_bytes_list_yr_uta_swt2
      failed_bytes_list_yr_uta_swt2 = [ ]
  if (done_bytes_list_yr_uta_swt2):
      done_bytes_list1_yr_uta_swt2 = done_bytes_list_yr_uta_swt2
      done_bytes_list_yr_uta_swt2 = [ ]
  if (planned_files_list_yr_uta_swt2):
     planned_files_list1_yr_uta_swt2 = planned_files_list_yr_uta_swt2
     planned_files_list_yr_uta_swt2 = [ ]
  if (failed_files_list_yr_uta_swt2):
     failed_files_list1_yr_uta_swt2 = failed_files_list_yr_uta_swt2
     failed_files_list_yr_uta_swt2 = [ ]
  if (done_files_list_yr_uta_swt2):
     done_files_list1_yr_uta_swt2 = done_files_list_yr_uta_swt2
     done_files_list_yr_uta_swt2 = [ ]

  planned_bytes_yr_uta_swt2=json.dumps(planned_bytes_list1_yr_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
  failed_bytes_yr_uta_swt2=json.dumps(failed_bytes_list1_yr_uta_swt2,indent=4, sort_keys =False, encoding='utf-8')
  done_bytes_yr_uta_swt2=json.dumps(done_bytes_list1_yr_uta_swt2,indent=4, sort_keys =False, encoding='utf-8')
  planned_files_yr_uta_swt2 = json.dumps(planned_files_list1_yr_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
  failed_files_yr_uta_swt2 = json.dumps(failed_files_list1_yr_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
  done_files_yr_uta_swt2 = json.dumps(done_files_list1_yr_uta_swt2, indent=4, sort_keys=False, encoding='utf-8')
  list_uta_swt2=json.dumps(list_uta_swt2,indent=4, sort_keys =False, encoding='utf-8')

  return list_uta_swt2,planned_bytes_yr_uta_swt2,failed_bytes_yr_uta_swt2,done_bytes_yr_uta_swt2,planned_files_yr_uta_swt2,failed_files_yr_uta_swt2,done_files_yr_uta_swt2

########################################################## OU_OSCER_ATLAS ################################################################
 db.del_OU_OSCER_ATLAS.find({}).sort("to_date", pymongo.ASCENDING)
 for x in db.del_OU_OSCER_ATLAS.find({"to_date": {"$gte":d2}}):
       planned_bytes = {
           'y': x[ "planned_bytes_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_bytes_list_ou_oscer.append(planned_bytes)
       failed_bytes ={
          'y': x[ "failed_bytes_xs" ],
          'x': str(x[ "to_date" ])

       }
       failed_bytes_list_ou_oscer.append(failed_bytes)
       done_bytes={
          'y':x["done_bytes_xs"],
          'x':str(x["to_date"])
       }
       done_bytes_list_ou_oscer.append(done_bytes)
       planned_files = {
           'y': x[ "planned_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_files_list_ou_oscer.append(planned_files)
       failed_files = {
           'y': x[ "failed_files_xs" ],
           'x': str(x[ "to_date" ])

       }
       failed_files_list_ou_oscer.append(failed_files)
       done_files = {
           'y': x[ "done_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       done_files_list_ou_oscer.append(done_files)
 if (planned_bytes_list_ou_oscer):
      planned_bytes_list1_ou_oscer = planned_bytes_list_ou_oscer
      planned_bytes_list_ou_oscer = [ ]
 if (failed_bytes_list_ou_oscer):
      failed_bytes_list1_ou_oscer = failed_bytes_list_ou_oscer
      failed_bytes_list_ou_oscer = [ ]
 if (done_bytes_list_ou_oscer):
      done_bytes_list1_ou_oscer = done_bytes_list_ou_oscer
      done_bytes_list_ou_oscer = [ ]
 if (planned_files_list_ou_oscer):
      planned_files_list1_ou_oscer = planned_files_list_ou_oscer
      planned_files_list_ou_oscer = [ ]
 if (failed_files_list_ou_oscer):
      failed_files_list1_ou_oscer = failed_files_list_ou_oscer
      failed_files_list_ou_oscer = [ ]
 if (done_files_list_ou_oscer):
      done_files_list1_ou_oscer = done_files_list_ou_oscer
      done_files_list_ou_oscer = [ ]

 planned_bytes_ou_oscer = json.dumps(planned_bytes_list1_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
 failed_bytes_ou_oscer = json.dumps(failed_bytes_list1_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
 done_bytes_ou_oscer = json.dumps(done_bytes_list1_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
 planned_files_ou_oscer = json.dumps(planned_files_list1_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
 failed_files_ou_oscer = json.dumps(failed_files_list1_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
 done_files_ou_oscer = json.dumps(done_files_list1_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
 # --------------------------------------------------------------------------------
 @classmethod
 def data_prep_ou_oscer(self):
  planned_bytes_list_yr_ou_oscer = [ ]
  planned_bytes_list1_yr_ou_oscer = [ ]
  failed_bytes_list_yr_ou_oscer = [ ]
  failed_bytes_list1_yr_ou_oscer = [ ]
  done_bytes_list_yr_ou_oscer = [ ]
  done_bytes_list1_yr_ou_oscer = [ ]
  planned_files_list_yr_ou_oscer = [ ]
  planned_files_list1_yr_ou_oscer = [ ]
  failed_files_list_yr_ou_oscer = [ ]
  failed_files_list1_yr_ou_oscer = [ ]
  done_files_list_yr_ou_oscer = [ ]
  done_files_list1_yr_ou_oscer = [ ]
  list_ou_oscer = [ ]

  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  db.del_OU_OSCER_ATLAS.find({}).sort("to_date", pymongo.ASCENDING)
  for x in db.del_OU_OSCER_ATLAS.find({"to_date": {"$gt": utc_dt_365}}):
        planned_bytes = {
            'y': x[ "planned_bytes_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_bytes'
        }
        planned_bytes_list_yr_ou_oscer.append(planned_bytes)
        failed_bytes ={
           'y': x[ "failed_bytes_xs" ],
           'x': str(x[ "to_date" ]),
           'source': 'failed_bytes'
        }
        failed_bytes_list_yr_ou_oscer.append(failed_bytes)
        done_bytes={
           'y':x["done_bytes_xs"],
           'x':str(x["to_date"]),
           'source':'done_bytes'
        }
        done_bytes_list_yr_ou_oscer.append(done_bytes)
        planned_files = {
            'y': x[ "planned_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_files'
        }
        planned_files_list_yr_ou_oscer.append(planned_files)
        list_ou_oscer.append(planned_files)
        failed_files = {
            'y': x[ "failed_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'failed_files'
        }
        failed_files_list_yr_ou_oscer.append(failed_files)
        list_ou_oscer.append(failed_files)
        done_files = {
            'y': x[ "done_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'done_files'
        }
        done_files_list_yr_ou_oscer.append(done_files)
        list_ou_oscer.append(done_files)


  if(planned_bytes_list_yr_ou_oscer):
      planned_bytes_list1_yr_ou_oscer=planned_bytes_list_yr_ou_oscer
      planned_bytes_list_yr_ou_oscer=[]
  if (failed_bytes_list_yr_ou_oscer):
      failed_bytes_list1_yr_ou_oscer= failed_bytes_list_yr_ou_oscer
      failed_bytes_list_yr_ou_oscer = [ ]
  if (done_bytes_list_yr_ou_oscer):
      done_bytes_list1_yr_ou_oscer = done_bytes_list_yr_ou_oscer
      done_bytes_list_yr_ou_oscer = [ ]
  if (planned_files_list_yr_ou_oscer):
     planned_files_list1_yr_ou_oscer = planned_files_list_yr_ou_oscer
     planned_files_list_yr_ou_oscer = [ ]
  if (failed_files_list_yr_ou_oscer):
     failed_files_list1_yr_ou_oscer = failed_files_list_yr_ou_oscer
     failed_files_list_yr_ou_oscer = [ ]
  if (done_files_list_yr_ou_oscer):
     done_files_list1_yr_ou_oscer = done_files_list_yr_ou_oscer
     done_files_list_yr_ou_oscer = [ ]

  planned_bytes_yr_ou_oscer=json.dumps(planned_bytes_list1_yr_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
  failed_bytes_yr_ou_oscer=json.dumps(failed_bytes_list1_yr_ou_oscer,indent=4, sort_keys =False, encoding='utf-8')
  done_bytes_yr_ou_oscer=json.dumps(done_bytes_list1_yr_ou_oscer,indent=4, sort_keys =False, encoding='utf-8')
  planned_files_yr_ou_oscer = json.dumps(planned_files_list1_yr_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
  failed_files_yr_ou_oscer = json.dumps(failed_files_list1_yr_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
  done_files_yr_ou_oscer = json.dumps(done_files_list1_yr_ou_oscer, indent=4, sort_keys=False, encoding='utf-8')
  list_ou_oscer=json.dumps(list_ou_oscer,indent=4, sort_keys =False, encoding='utf-8')

  return list_ou_oscer,planned_bytes_yr_ou_oscer,failed_bytes_yr_ou_oscer,done_bytes_yr_ou_oscer,planned_files_yr_ou_oscer,failed_files_yr_ou_oscer,done_files_yr_ou_oscer


########################################################## LUCILLE ################################################################
 db.del_LUCILLE.find({}).sort("to_date", pymongo.ASCENDING)
 for x in db.del_LUCILLE.find({"to_date": {"$gte":d2}}):
       planned_bytes = {
           'y': x[ "planned_bytes_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_bytes_list_luccile.append(planned_bytes)
       failed_bytes ={
          'y': x[ "failed_bytes_xs" ],
          'x': str(x[ "to_date" ])

       }
       failed_bytes_list_luccile.append(failed_bytes)
       done_bytes={
          'y':x["done_bytes_xs"],
          'x':str(x["to_date"])
       }
       done_bytes_list_luccile.append(done_bytes)
       planned_files = {
           'y': x[ "planned_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       planned_files_list_luccile.append(planned_files)
       failed_files = {
           'y': x[ "failed_files_xs" ],
           'x': str(x[ "to_date" ])

       }
       failed_files_list_luccile.append(failed_files)
       done_files = {
           'y': x[ "done_files_xs" ],
           'x': str(x[ "to_date" ])
       }
       done_files_list_luccile.append(done_files)
 if (planned_bytes_list_luccile):
      planned_bytes_list1_luccile = planned_bytes_list_luccile
      planned_bytes_list_luccile = [ ]
 if (failed_bytes_list_luccile):
      failed_bytes_list1_luccile = failed_bytes_list_luccile
      failed_bytes_list_luccile = [ ]
 if (done_bytes_list_luccile):
      done_bytes_list1_luccile= done_bytes_list_luccile
      done_bytes_list_luccile = [ ]
 if (planned_files_list_luccile):
      planned_files_list1_luccile = planned_files_list_luccile
      planned_files_list_luccile = [ ]
 if (failed_files_list_luccile):
      failed_files_list1_luccile = failed_files_list_luccile
      failed_files_list_luccile = [ ]
 if (done_files_list_luccile):
      done_files_list1_luccile= done_files_list_luccile
      done_files_list_luccile = [ ]

 planned_bytes_luccile = json.dumps(planned_bytes_list1_luccile, indent=4, sort_keys=False, encoding='utf-8')
 failed_bytes_luccile = json.dumps(failed_bytes_list1_luccile, indent=4, sort_keys=False, encoding='utf-8')
 done_bytes_luccile = json.dumps(done_bytes_list1_luccile, indent=4, sort_keys=False, encoding='utf-8')
 planned_files_luccile = json.dumps(planned_files_list1_luccile, indent=4, sort_keys=False, encoding='utf-8')
 failed_files_luccile = json.dumps(failed_files_list1_luccile, indent=4, sort_keys=False, encoding='utf-8')
 done_files_luccile = json.dumps(done_files_list1_luccile, indent=4, sort_keys=False, encoding='utf-8')
 # --------------------------------------------------------------------------------
 @classmethod
 def data_prep_lucille(self):
  planned_bytes_list_yr_luccile = [ ]
  planned_bytes_list1_yr_luccile = [ ]
  failed_bytes_list_yr_luccile = [ ]
  failed_bytes_list1_yr_luccile = [ ]
  done_bytes_list_yr_luccile = [ ]
  done_bytes_list1_yr_luccile = [ ]
  planned_files_list_yr_luccile = [ ]
  planned_files_list1_yr_luccile = [ ]
  failed_files_list_yr_luccile = [ ]
  failed_files_list1_yr_luccile = [ ]
  done_files_list_yr_luccile = [ ]
  done_files_list1_yr_luccile = [ ]
  list_luccile = [ ]

  delta = s.read.readDays()
  utc_dt_365 = d.utcnow() + ((-1) * timedelta(delta))

  db.del_LUCILLE.find({}).sort("to_date", pymongo.ASCENDING)
  for x in db.del_LUCILLE.find({"to_date": {"$gt": utc_dt_365}}):
        planned_bytes = {
            'y': x[ "planned_bytes_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_bytes'
        }
        planned_bytes_list_yr_luccile.append(planned_bytes)
        failed_bytes ={
           'y': x[ "failed_bytes_xs" ],
           'x': str(x[ "to_date" ]),
           'source': 'failed_bytes'
        }
        failed_bytes_list_yr_luccile.append(failed_bytes)
        done_bytes={
           'y':x["done_bytes_xs"],
           'x':str(x["to_date"]),
           'source':'done_bytes'
        }
        done_bytes_list_yr_luccile.append(done_bytes)
        planned_files = {
            'y': x[ "planned_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'planned_files'
        }
        planned_files_list_yr_luccile.append(planned_files)
        list_luccile.append(planned_files)
        failed_files = {
            'y': x[ "failed_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'failed_files'
        }
        failed_files_list_yr_luccile.append(failed_files)
        list_luccile.append(failed_files)
        done_files = {
            'y': x[ "done_files_xs" ],
            'x': str(x[ "to_date" ]),
            'source': 'done_files'
        }
        done_files_list_yr_luccile.append(done_files)
        list_luccile.append(done_files)


  if(planned_bytes_list_yr_luccile):
      planned_bytes_list1_yr_luccile=planned_bytes_list_yr_luccile
      planned_bytes_list_yr_luccile=[]
  if (failed_bytes_list_yr_luccile):
      failed_bytes_list1_yr_luccile = failed_bytes_list_yr_luccile
      failed_bytes_list_yr_luccile = [ ]
  if (done_bytes_list_yr_luccile):
      done_bytes_list1_yr_luccile = done_bytes_list_yr_luccile
      done_bytes_list_yr_luccile = [ ]
  if (planned_files_list_yr_luccile):
     planned_files_list1_yr_luccile = planned_files_list_yr_luccile
     planned_files_list_yr_luccile = [ ]
  if (failed_files_list_yr_luccile):
     failed_files_list1_yr_luccile = failed_files_list_yr_luccile
     failed_files_list_yr_luccile = [ ]
  if (done_files_list_yr_luccile):
     done_files_list1_yr_luccile = done_files_list_yr_luccile
     done_files_list_yr_luccile = [ ]


  planned_bytes_yr_luccile=json.dumps(planned_bytes_list1_yr_luccile, indent=4, sort_keys=False, encoding='utf-8')
  failed_bytes_yr_luccile=json.dumps(failed_bytes_list1_yr_luccile,indent=4, sort_keys =False, encoding='utf-8')
  done_bytes_yr_luccile=json.dumps(done_bytes_list1_yr_luccile,indent=4, sort_keys =False, encoding='utf-8')
  planned_files_yr_luccile = json.dumps(planned_files_list1_yr_luccile, indent=4, sort_keys=False, encoding='utf-8')
  failed_files_yr_luccile = json.dumps(failed_files_list1_yr_luccile, indent=4, sort_keys=False, encoding='utf-8')
  done_files_yr_luccile = json.dumps(done_files_list1_yr_luccile, indent=4, sort_keys=False, encoding='utf-8')
  list_luccile=json.dumps(list_luccile,indent=4, sort_keys =False, encoding='utf-8')
  return list_luccile,planned_bytes_yr_luccile,failed_bytes_yr_luccile,done_bytes_yr_luccile,planned_files_yr_luccile,failed_files_yr_luccile,done_files_yr_luccile
