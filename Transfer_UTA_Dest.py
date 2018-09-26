import json,os,requests
from pymongo import MongoClient
from dateutil import parser

client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']



class Transfer_UTA_Dest:

 for a in db.url.find({'x':'del_lh'}):
  url =a["y"]

  b = requests.get(url).json()
  key_transfer=[]
  key_transfer1=[]
  row1=[]
  item1 = [ ]
  src_clouds = [ ]
  dst_sites = [ ]
  x=0
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
          if key_transfer[ i ] == "src_cloud":
              src_cloud = row1[ key_transfer1[ i ] ]
      for i in key_transfer1:
          if key_transfer[ i ] == "dst_site":
              dst_site = row1[ key_transfer1[ i ] ]
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
          'src_cloud': src_cloud,
          'dst_site': dst_site,
          'x':x

      }
      item1.append(item)


  y1=[]
  y2=[]
  y3=[]
  data=[]
  while(item1):
   x=item1.pop()
   if(x['dst_site']=='UTA_SWT2'):
       if(x['src_cloud'] == 'US'):
           z=str(x['src_cloud'])+'^'+str(x['x'])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'CERN'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'DE'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'ES'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'CA'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'RU'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'UK'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'IT'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'ND'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'FR'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'NL'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)
       elif (x[ 'src_cloud' ] == 'TW'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y1.append(z)

   if(x[ 'dst_site' ] == 'OU_OSCER_ATLAS'):
       if (x[ 'src_cloud' ] == 'US'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       elif (x[ 'src_cloud' ] == 'CERN'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'DE'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'ES'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'CA'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'RU'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'UK'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'IT'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'ND'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'FR'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'NL'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)
       if (x[ 'src_cloud' ] == 'TW'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y2.append(z)

   if(x[ 'dst_site' ] == 'SWT2_CPB'):
       if (x[ 'src_cloud' ] == 'US'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'CERN'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'DE'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'ES'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'CA'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'RU'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'UK'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'IT'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'ND'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'FR'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'NL'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
           y3.append(z)
       if (x[ 'src_cloud' ] == 'TW'):
           z = str(x[ 'src_cloud' ]) + '^' + str(x[ 'x' ])
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
