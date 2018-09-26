import json,io
import requests
from pymongo import MongoClient
from datetime import *

client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
# DDM JSON URL for our sites as a destination AND deletions (LAST HOUR)
class tran:
 for a in db.url.find({'x':'tran_lh'}):
  url =a["y"]

 b = requests.get(url).json()

 # key_deletions=[]
 # key_deletions1=[]
 # row1=[]
 # row2=[]
 # row3=[]
 # planned_bytes_list = []
 # planned_bytes_list1=[]
 # failed_bytes_list=[]
 # failed_bytes_list1=[]
 # done_bytes_list=[]
 # done_bytes_list1=[]
 #
 # planned_bytes_list_yr = [ ]
 # planned_bytes_list1_yr = [ ]
 # failed_bytes_list_yr = [ ]
 # failed_bytes_list1_yr = [ ]
 # done_bytes_list_yr = [ ]
 # done_bytes_list1_yr = [ ]
 #
 # to_date=b['params']['to_date']
 # to_date1=datetime.strptime(to_date,'%Y-%m-%dT%X')
 # rows= len(b['deletions']['rows'])
 # myList = [ [ ] for i in range(rows) ]
 # for a in range(0,rows,1):
 #    for k in b[ 'deletions' ][ 'rows' ][ a ]:
 #        myList[a].append(k)
 # myList.reverse()
 # for i in b['deletions']['key']:
 #  key_deletions.append(i)
 #  key_deletions1.append(b['deletions']['key'][i])
 # for a in range(0,rows,1):
 #  row1=myList.pop()
 #  for i in key_deletions1:
 #
 #   if key_deletions[i]=="planned_bytes_xs":
 #    SWT2_CPB_planned_bytes=row1[key_deletions1[i]]
 #   elif key_deletions[i]=="failed_bytes_xs":
 #    SWT2_CPB_failed_bytes = row1[ key_deletions1[ i ] ]
 #   elif key_deletions[i]=="done_bytes_xs":
 #    SWT2_CPB_done_bytes=row1[key_deletions1[i]]
 #  result = db.del_SWT2_CPB.insert_one(
 #        {
 #            "planned_bytes_xs": SWT2_CPB_planned_bytes,
 #            "failed_bytes_xs":SWT2_CPB_failed_bytes,
 #            "done_bytes_xs":SWT2_CPB_done_bytes,
 #            "to_date":to_date1
 #        }
 #    );
 #  d = datetime.now() + timedelta(days=-7)
 #  for x in db.del_SWT2_CPB.find({"to_date": {"$gt": d }}):
 #       planned_bytes = {
 #           'y': x[ "planned_bytes_xs" ],
 #           'x': str(x[ "to_date" ])
 #       }
 #       planned_bytes_list.append(planned_bytes)
 #       failed_bytes ={
 #          'y': x[ "failed_bytes_xs" ],
 #          'x': str(x[ "to_date" ])
 #
 #       }
 #       failed_bytes_list.append(failed_bytes)
 #       done_bytes={
 #          'y':x["done_bytes_xs"],
 #          'x':str(x["to_date"])
 #       }
 #       done_bytes_list.append(done_bytes)
 #
 #  if (planned_bytes_list):
 #      planned_bytes_list1 = planned_bytes_list
 #      planned_bytes_list = [ ]
 #  if (failed_bytes_list):
 #      failed_bytes_list1 = failed_bytes_list
 #      failed_bytes_list = [ ]
 #  if (done_bytes_list):
 #      done_bytes_list1 = done_bytes_list
 #      done_bytes_list = [ ]
 #  # --------------------------------------------------------------------------------
 #  for x in db.del_SWT2_CPB.find({"to_date": {"$ne": None}}):
 #        planned_bytes = {
 #            'y': x[ "planned_bytes_xs" ],
 #            'x': str(x[ "to_date" ])
 #        }
 #        planned_bytes_list_yr.append(planned_bytes)
 #        failed_bytes ={
 #           'y': x[ "failed_bytes_xs" ],
 #           'x': str(x[ "to_date" ])
 #
 #        }
 #        failed_bytes_list_yr.append(failed_bytes)
 #        done_bytes={
 #           'y':x["done_bytes_xs"],
 #           'x':str(x["to_date"])
 #        }
 #        done_bytes_list_yr.append(done_bytes)
 #
 #
 #
 #  if(planned_bytes_list_yr):
 #      planned_bytes_list1_yr=planned_bytes_list_yr
 #      planned_bytes_list_yr=[]
 #  if (failed_bytes_list_yr):
 #      failed_bytes_list1_yr = failed_bytes_list_yr
 #      failed_bytes_list_yr = [ ]
 #  if (done_bytes_list_yr):
 #      done_bytes_list1_yr = done_bytes_list_yr
 #      done_bytes_list_yr = [ ]
 #
 #
 #  l=json.dumps(planned_bytes_list1, indent=4, sort_keys=False, encoding='utf-8')
 #  m=json.dumps(failed_bytes_list1,indent=4, sort_keys =False, encoding='utf-8')
 #  n=json.dumps(done_bytes_list1,indent=4, sort_keys =False, encoding='utf-8')
 #  o=json.dumps(planned_bytes_list1_yr, indent=4, sort_keys=False, encoding='utf-8')
 #  p=json.dumps(failed_bytes_list1_yr,indent=4, sort_keys =False, encoding='utf-8')
 #  q=json.dumps(done_bytes_list1_yr,indent=4, sort_keys =False, encoding='utf-8')
 #
 #
