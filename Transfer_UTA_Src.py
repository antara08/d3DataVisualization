import json,io,os,requests
from pymongo import MongoClient
from dateutil import parser
import ConfigParser
dirname=os.getcwd()
#dirname = os.path.dirname(__file__)

client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']



class Transfer_UTA_Src:

 for a in db.url.find({'x':'tran_lh'}):
  url =a["y"]

  b = requests.get(url).json()
  key_transfer=[]
  key_transfer1=[]
  x=0
  row1=[]
  item1 = [ ]
  src_clouds = [ ]
  dst_sites = [ ]
  to_date = parser.parse(b[ 'params' ][ 'to_date' ])
  rows = len(b[ 'transfers' ][ 'rows' ])
  myList = [ [ ] for i in range(rows) ]
  for a in range(0, rows, 1):
      for k in b[ 'transfers' ][ 'rows' ][ a ]:
          myList[ a ].append(k)
  myList.reverse()
  for i in b[ 'transfers' ][ 'key' ]:
      key_transfer.append(i)
      key_transfer1.append(b[ 'transfers' ][ 'key' ][ i ])
  for a in range(0, rows, 1):
      row1 = myList.pop()
      to_date = parser.parse(b[ 'params' ][ 'to_date' ])
      for i in key_transfer1:
          if key_transfer[ i ] == "src_site":
              src_site = row1[ key_transfer1[ i ] ]
      for i in key_transfer1:
          if key_transfer[ i ] == "dst_cloud":
              dst_cloud = row1[ key_transfer1[ i ] ]
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
      if (files_xs != 0):
              x = round((files_xs / float(errors_xs + files_xs))*100,2)


      item={
          'src_site': src_site,
          'dst_cloud': dst_cloud,
          'x':x

      }
      item1.append(item)

  y1=[]
  y2=[]
  y3=[]
  data=[]
  while(item1):
   x=item1.pop()
   if(x['src_site']=='UTA_SWT2'):
       if(x['dst_cloud'] == 'US'):
           z=str(x['dst_cloud'])+'^'+str(x['x'])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'CERN'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'DE'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'ES'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'CA'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'RU'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'UK'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'IT'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'ND'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'FR'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'NL'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'dst_cloud' ] == 'TW'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)

   if(x[ 'src_site' ] == 'OU_OSCER_ATLAS'):
       if (x[ 'dst_cloud' ] == 'US'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       elif (x[ 'dst_cloud' ] == 'CERN'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'DE'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'ES'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'CA'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'RU'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'UK'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'IT'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'ND'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'FR'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'NL'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'dst_cloud' ] == 'TW'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)

   if(x[ 'src_site' ] == 'SWT2_CPB'):
       if (x[ 'dst_cloud' ] == 'US'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'CERN'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'DE'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'ES'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'CA'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'RU'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'UK'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'IT'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'ND'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'FR'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'NL'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'dst_cloud' ] == 'TW'):
           z = str(x[ 'dst_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
  l = len(y1)
  m = len(y2)
  n = len(y3)

  cl=['CA','CERN','DE','ES','FR','IT','ND','NL','RU','TW','UK','US']
  for i in range(0,len(cl)):
     ismatch=False
     cle=cl[i]

     for j in range(0,l ):
         if(cle in y1[j]):
             ismatch=True
             break
     if(ismatch==False):
      q=cle+'^0'
      y1.append(q)

  for i in range(0,len(cl)):
     ismatch=False
     cle=cl[i]

     for j in range(0,m):
         if(cle in y2[j]):
             ismatch=True
             break
     if(ismatch==False):
      q=cle+'^0'
      y2.append(q)

  for i in range(0,len(cl)):
     ismatch=False
     cle=cl[i]

     for j in range(0,n):
         if(cle in y3[j]):
             ismatch=True
             break
     if(ismatch==False):
      q=cle+'^0'
      y3.append(q)

  y1.sort()
  y2.sort()
  y3.sort()

  data=[
       {
           'x':y1,
           'y':'UTA_SWT2'
       },
      {
          'x':y2,
          'y':'OU_OSCER_ATLAS'
      },
      {
          'x':y3,
          'y':'SWT2_CPB'
      }

   ]

  data1=json.dumps(data, indent=4, sort_keys=False, encoding='utf-8')
