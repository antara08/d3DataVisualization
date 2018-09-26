import requests,pymongo
from pymongo import MongoClient
from dateutil import parser
import sendMail

client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
# DDM JSON URL for our sites as a destination AND deletions (LAST HOUR)
class fetchData_Deletion:
 for a in db.url.find({'x':'del_lh'}):
  url =a["y"]

 b = requests.get(url).json()

 key_deletions=[]
 key_deletions1=[]
 row1=[]
 planned_bytes_list = []
 planned_bytes_list1=[]
 failed_bytes_list=[]
 failed_bytes_list1=[]
 done_bytes_list=[]
 done_bytes_list1=[]
 planned_files_list=[]
 planned_files_list1=[]
 done_files_list=[]
 done_files_list1=[]
 failed_files_list=[]
 failed_files_list1=[]

 planned_bytes_list_yr = [ ]
 planned_bytes_list1_yr = [ ]
 failed_bytes_list_yr = [ ]
 failed_bytes_list1_yr = [ ]
 done_bytes_list_yr = [ ]
 done_bytes_list1_yr = [ ]
 mail=sendMail.sendMail()

 to_date=parser.parse(b['params']['to_date'])
 #to_date1=datetime.strptime(to_date,'%Y-%m-%dT%X')
 rows= len(b['deletions']['rows'])
 myList = [ [ ] for i in range(rows) ]
 for a in range(0,rows,1):
    for k in b[ 'deletions' ][ 'rows' ][ a ]:
        myList[a].append(k)
 myList.reverse()

 for i in b['deletions']['key']:
  key_deletions.append(i)
  key_deletions1.append(b['deletions']['key'][i])
 for a in range(0,rows,1):
  row1=myList.pop()
  for i in key_deletions1:
   if key_deletions[i]=="planned_bytes_xs":
    planned_bytes=row1[key_deletions1[i]]
   elif key_deletions[i]=="failed_bytes_xs":
    failed_bytes = row1[ key_deletions1[ i ] ]
   elif key_deletions[i]=="done_bytes_xs":
    done_bytes=row1[key_deletions1[i]]
   elif key_deletions[i]=="dst_site":
    database=row1[key_deletions1[i]]
   elif key_deletions[i]=="failed_files_xs":
    failed_files=row1[key_deletions1[i]]
   elif key_deletions[i]=="planned_files_xs":
    planned_files=row1[key_deletions1[i]]
   elif key_deletions[i]=="done_files_xs":
    done_files=row1[key_deletions1[i]]
  if(database):
     if(database=='SWT2_CPB'):
      if(done_files):
       n=(failed_bytes/done_bytes)*100
       if(n>10):
        mail.mail("Rate failure of deletion at SWT2_CPB : " + str(round(n,2)) + "%")
      elif (done_files==0 and failed_files!=0):
       mail.mail("The total done files in the last hour for SWT2_CPB is:"+ str(done_files)+" files" + "and failed files is:"+str(failed_files)+" files")
      try:
       result = db.del_SWT2_CPB.insert_one(
        {
            "planned_bytes_xs": planned_bytes,
            "failed_bytes_xs":failed_bytes,
            "done_bytes_xs":done_bytes,
            "failed_files_xs": failed_files,
            "planned_files_xs":planned_files,
            "done_files_xs":done_files,
            "to_date":to_date
        }
       );
      except pymongo.errors.DuplicateKeyError:
       pass
     elif(database=='UTA_SWT2'):
      if(done_files):
       n = (failed_bytes / done_bytes) * 100
       if (n > 10):
        mail.mail("Rate failure of deletion at UTA_SWT2 : " + str(round(n,2)) + "%")
      elif (done_files==0 and failed_files!=0):
       mail.mail("The total done files in the last hour for UTA_SWT2 is:"+ str(done_files)+" files" + "and failed files is:"+str(failed_files)+" files")
      try:
       result = db.del_UTA_SWT2.insert_one(
       {
        "planned_bytes_xs": planned_bytes,
        "failed_bytes_xs": failed_bytes,
        "done_bytes_xs": done_bytes,
        "failed_files_xs":failed_files,
        "planned_files_xs": planned_files,
        "done_files_xs": done_files,
        "to_date": to_date
       }
       );
      except pymongo.errors.DuplicateKeyError:
       pass

     elif (database == 'OU_OSCER_ATLAS'):
      if(done_files):
       n = (failed_bytes / done_bytes) * 100
       if (n > 10):
        mail.mail("Rate failure of deletion at OU_OSCER_ATLAS : " + str(round(n,2)) + "%")
      elif (done_files==0 and failed_files!=0):
       mail.mail("The total done files in the last hour for OU_OSCER_ATLAS is:"+ str(done_files)+" files" + "and failed files is:"+str(failed_bytes)+" files")
      try:
       result = db.del_OU_OSCER_ATLAS.insert_one(
       {
        "planned_bytes_xs": planned_bytes,
        "failed_bytes_xs": failed_bytes,
        "done_bytes_xs": done_bytes,
        "failed_files_xs": failed_files,
        "planned_files_xs": planned_files,
        "done_files_xs": done_files,
        "to_date": to_date
       }
        );
      except pymongo.errors.DuplicateKeyError:
       pass
     elif (database == 'LUCILLE'):
      if (done_files):
       n = (failed_bytes / done_bytes) * 100
       if (n > 10):
        mail.mail("Rate failure of deletion at LUCILLE : " + str(round(n,2)) + "%")
      elif (done_files==0 and failed_files!=0):
       mail.mail("The total done files in the last hour for LUCILLE is:"+ str(done_files)+" files" + "and failed files is:"+str(failed_files)+" files")
      try:
       result = db.del_LUCILLE.insert_one(
       {
        "planned_bytes_xs": planned_bytes,
        "failed_bytes_xs": failed_bytes,
        "done_bytes_xs": done_bytes,
        "failed_files_xs": failed_files,
        "planned_files_xs": planned_files,
        "done_files_xs": done_files,
        "to_date": to_date
       }
       );
      except pymongo.errors.DuplicateKeyError:
       pass