import requests
from pymongo import MongoClient
from datetime import *
import sendMail



client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
class fetchData_Transfer:
 for a in db.url.find({'x':'tran_lh'}):
  url =a["y"]

 b = requests.get(url).json()
 key_transfer=[]
 key_transfer1=[]
 row1=[]
 row2=[]
 row3=[]
 planned_bytes_list = []
 planned_bytes_list1=[]
 failed_bytes_list=[]
 failed_bytes_list1=[]
 done_bytes_list=[]
 done_bytes_list1=[]

 planned_bytes_list_yr = [ ]
 planned_bytes_list1_yr = [ ]
 failed_bytes_list_yr = [ ]
 failed_bytes_list1_yr = [ ]
 done_bytes_list_yr = [ ]
 done_bytes_list1_yr = [ ]
 tableList=[]
 mail=sendMail.sendMail()

 to_date=b['params']['to_date']
 to_date1=datetime.strptime(to_date,'%Y-%m-%dT%X')
 rows= len(b['transfers']['rows'])
 myList = [ [ ] for i in range(rows) ]
 for a in range(0,rows,1):
    for k in b[ 'transfers' ][ 'rows' ][ a ]:
        myList[a].append(k)
 myList.reverse()
 for i in b['transfers']['key']:
  key_transfer.append(i)
  key_transfer1.append(b['transfers']['key'][i])

 for a in range(0,rows,1):
  row1=myList.pop()
  for i in key_transfer1:
   if key_transfer[i]=="src_site":
    src_site=row1[key_transfer1[i]]
  for i in key_transfer1:
   if key_transfer[i]=="dst_cloud":
    dst_cloud=row1[key_transfer1[i]]
  x=src_site+"_"+dst_cloud
  #number of errors
  for i in key_transfer1:
   if key_transfer[i]=="errors_xs":
    errors_xs=row1[key_transfer1[i]]
  #number of successes
  for i in key_transfer1:
    if key_transfer[ i ] == "files_xs":
     files_xs = row1[ key_transfer1[ i ] ]
  for i in key_transfer1:
   if key_transfer[i]=="bytes_xs":
     bytes_xs=row1[key_transfer1[i]]
  if (db.Transfer_Tables.find({"table": {"$ne": x}})):
      tableList.append(x)
      db.Transfer_Tables.insert_one(
          {
              "table": x
          }
      );
  tableList1=[]
  tableList1=tableList
  while(tableList1):
      y=tableList1.pop()
      for i in key_transfer1:
          if key_transfer[ i ] == "src_site":
              src_site = row1[ key_transfer1[ i ] ]
      for i in key_transfer1:
          if key_transfer[ i ] == "dst_cloud":
              dst_cloud = row1[ key_transfer1[ i ] ]
      x = src_site + "_" + dst_cloud
      for i in key_transfer1:
          if key_transfer[ i ] == "errors_xs":
              errors_xs = row1[ key_transfer1[ i ] ]
      # number of successes
      for i in key_transfer1:
          if key_transfer[ i ] == "files_xs":
              files_xs = row1[ key_transfer1[ i ] ]
      for i in key_transfer1:
          if key_transfer[ i ] == "bytes_xs":
              bytes_xs = row1[ key_transfer1[ i ] ]
      if(x==y):
          db[x].insert_one(
              {
                  "errors_xs":errors_xs,
                  "files_xs":files_xs,
                  "bytes_xs":bytes_xs

              }
          )


  if(errors_xs!=0):
    if(files_xs!=0):
      x=errors_xs/float(errors_xs+files_xs)
      if((x*100)>10):
        mail.mail("This requires your attention.Failure of transfer of data between source site " + src_site + " and destination cloud "+dst_cloud+ " greater than 10%")
