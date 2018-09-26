import pymongo
import requests
from pymongo import MongoClient
import sendMail
from dateutil import parser


client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
class fetchData_Transfer:
 for a in db.url.find({'x':'del_lh'}):
  url =a["y"]

 b = requests.get(url).json()
 key_transfer=[]
 key_transfer1=[]
 row1=[]
 tableList=[]
 mail=sendMail.sendMail()
 x=0
 error_prcnt=0

 to_date=parser.parse(b['params']['to_date'])
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
  error_prcnt=0
  to_date = parser.parse(b[ 'params' ][ 'to_date' ])
  for i in key_transfer1:
   if key_transfer[i]=="src_cloud":
       src_cloud=row1[key_transfer1[i]]
  for i in key_transfer1:
   if key_transfer[i]=="dst_site":
       dst_site=row1[key_transfer1[i]]
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
  try:
      db.src_cloud_UTA_Dest.insert_one(
          {
              "src_cloud": src_cloud
          }
      );
  except pymongo.errors.DuplicateKeyError:
         pass
  try:
      db.dst_site_UTA_Dest.insert_one(
          {
              "dst_site": dst_site
          }

      );
  except pymongo.errors.DuplicateKeyError:
         pass
  if (errors_xs != 0):
      if (files_xs != 0):
          x = errors_xs / float(errors_xs + files_xs)
          error_prcnt = x * 100
          if((error_prcnt)>70):
           mail.mail("Error in Transfer rate of files between source: "+src_cloud+" and destination: "+dst_site+" is: "+str(round(error_prcnt,2))+"%"+" and the value of error_xs is:"+str(errors_xs)+" and the value of files_xs is:"+str(files_xs))
  try:
    db.Transfer_Tables_UTA_Dest.insert_one({
        'src_cloud':src_cloud,
        'dst_site':dst_site,
        'errors_xs':errors_xs,
        'files_xs':files_xs,
        'bytes_xs':bytes_xs,
        'error_prcnt':error_prcnt,
        'to_date':to_date
    })
  except pymongo.errors.DuplicateKeyError:
          pass
