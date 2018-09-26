import os,requests
import pymongo
from pymongo import MongoClient
from dateutil import parser
from pymongo.errors import DuplicateKeyError
import sendMail
#dirname = os.path.dirname(__file__)
dirname=os.getcwd()
import ConfigParser
Config = ConfigParser.ConfigParser()


client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']


class fetchData_Storage:
 rse_all=[]
 filename = dirname + '/config.cfg'
 Config.read(filename)
 url = Config.get("fetchData_Storage", "url")
 datadisk_offby=Config.get("swt2_cpb","datadisk_offby")
 alert_percentage=Config.get("swt2_cpb","datadisk_storage_percentage")
 wjdata = requests.get(url).json()  #fetches the json from the url and stores in wjdata
 json_SWT2_CPB_DATADISK = wjdata[ 'RSEDATA' ][ 'SWT2_CPB_DATADISK' ][ 'json' ][ 'total' ]
 db.json_total.update_one({"space_token": 'json_SWT2_CPB_DATADISK'},
                          {"$set": {
                              "space_token": 'json_SWT2_CPB_DATADISK',
                              "total": json_SWT2_CPB_DATADISK
                          }});
 json_SWT2_CPB_LOCALGROUPDISK = wjdata[ 'RSEDATA' ][ 'SWT2_CPB_LOCALGROUPDISK' ][ 'json' ][ 'total' ]
 db.json_total.update_one({"space_token": 'json_SWT2_CPB_LOCALGROUPDISK'},
                          {"$set": {
                              "space_token": 'json_SWT2_CPB_LOCALGROUPDISK',
                              "total": json_SWT2_CPB_LOCALGROUPDISK
                          }});
 json_SWT2_CPB_SCRATCHDISK = wjdata[ 'RSEDATA' ][ 'SWT2_CPB_SCRATCHDISK' ][ 'json' ][ 'total' ]
 db.json_total.update_one({"space_token": 'json_SWT2_CPB_SCRATCHDISK'},
                          {"$set": {
                              "space_token": 'json_SWT2_CPB_SCRATCHDISK',
                              "total": json_SWT2_CPB_SCRATCHDISK
                          }});
 json_UTA_SWT2_DATADISK = wjdata[ 'RSEDATA' ][ 'UTA_SWT2_DATADISK' ][ 'json' ][ 'total' ]
 db.json_total.update_one({"space_token": 'json_UTA_SWT2_DATADISK'},
                          {"$set": {
                              "space_token": 'json_UTA_SWT2_DATADISK',
                              "total": json_UTA_SWT2_DATADISK
                          }});
 mail=sendMail.sendMail()
 ################################################Fetch Data for SWT2_CPB_DATADISK#####################################################################

 SWT2_CPB_DATADISK = wjdata[ 'RSEDATA' ][ 'SWT2_CPB_DATADISK' ]
 for j in SWT2_CPB_DATADISK:
    rse_all.append(j)
 for i in SWT2_CPB_DATADISK:
    if i == 'rucio':
        rucio_used = (SWT2_CPB_DATADISK[ i ][ 'used' ])
        rucio_updated_at = parser.parse(SWT2_CPB_DATADISK[ i ][ 'updated_at' ])
        n = float((float(rucio_used) / int(json_SWT2_CPB_DATADISK)) * 100)
        result1=0
        try:
         result1 = db.rucio_SWT2_CPB_DATADISK.insert_one(
            {
                "updated_at": rucio_updated_at,
                "used": rucio_used
            }
         );
         if(result1):
          if (n > 95):
            mail.mail("Rucio SWT2_CPB_DATADISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError :
            pass
    elif i == 'json':
        json_used = (SWT2_CPB_DATADISK[ i ][ 'used' ])
        json_updated_at = parser.parse(SWT2_CPB_DATADISK[ i ][ 'updated_at' ])
        n = float((float(json_used) / int(json_SWT2_CPB_DATADISK)) * 100)
        result2=0
        try:
         result2 = db.json_SWT2_CPB_DATADISK.insert_one(
            {
                "updated_at": json_updated_at,
                "used": json_used
            }
         );
         if(result2):
             if (n > 95):
                 mail.mail("JSON SWT2_CPB_DATADISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError :
            pass
        if (result1 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
            if (result2 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                if ((((rucio_used - json_used) / int(json_SWT2_CPB_DATADISK)) * 100 > 10) or (
                        ((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                    mail.mail("Difference between Rucio and JSON in SWT2_CPB_DATADISK space token is"+str(round((((rucio_used-json_used)/int(json_SWT2_CPB_DATADISK))*100),2))+"% or off by "+((rucio_used-json_used)/1024 / 1024 / 1024 / 1024)+"TB")
    elif i == 'expired':
        expired_used = (SWT2_CPB_DATADISK[ i ][ 'used' ])
        expired_updated_at = parser.parse(SWT2_CPB_DATADISK[ i ][ 'updated_at' ])
        n = float((float(expired_used) /int(json_SWT2_CPB_DATADISK)) * 100)
        result3=0
        try:
         result3 = db.expired_SWT2_CPB_DATADISK.insert_one(
            {
                "updated_at": expired_updated_at,
                "used": expired_used
            }
         );
         if(result3):
          if (n > 95):
            mail.mail("Expired SWT2_CPB_DATADISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError :
            pass

    elif i == 'unavailable':
        unavailable_used = (SWT2_CPB_DATADISK[ i ][ 'used' ])
        unavailable_updated_at =parser.parse(SWT2_CPB_DATADISK[ i ][ 'updated_at' ])
        n = float((float(unavailable_used) / int(json_SWT2_CPB_DATADISK)) * 100)
        result4=0
        try:
         result4 = db.unavailable_SWT2_CPB_DATADISK.insert_one(
            {
                "updated_at": unavailable_updated_at,
                "used": unavailable_used
            }
         );
         if(result4):
          if (n > 95):
            mail.mail("Unavailable SWT2_CPB_DATADISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError :
            pass
    elif i == 'gsiftp':
        gsiftp_used = (SWT2_CPB_DATADISK[ i ][ 'used' ])
        gsiftp_updated_at = parser.parse(SWT2_CPB_DATADISK[ i ][ 'updated_at' ])
        n = float((float(gsiftp_used) / int(json_SWT2_CPB_DATADISK)) * 100)
        result5=0
        try:
         result5 = db.gsiftp_SWT2_CPB_DATADISK.insert_one(
            {
                "updated_at": gsiftp_updated_at,
                "used": gsiftp_used
            }
         );
         if(result5):
          if (n > 95):
            mail.mail("GSIFTP SWT2_CPB_DATADISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError :
            pass
    elif i == 'obsolete':
        obsolete_used = (SWT2_CPB_DATADISK[ i ][ 'used' ])
        obsolete_updated_at = parser.parse(SWT2_CPB_DATADISK[ i ][ 'updated_at' ])
        n = float((float(obsolete_used) / int(json_SWT2_CPB_DATADISK)) * 100)
        result6=0
        try:
         result6 = db.obsolete_SWT2_CPB_DATADISK.insert_one(
            {
                "updated_at": obsolete_updated_at,
                "used": obsolete_used
            }
         );
         if(result6):
          if (n > 95):
            mail.mail("Obsolete SWT2_CPB_DATADISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError :
            pass
 rse_all=[]
 rucio_used = 0
 json_used = 0
 gsiftp_used=0
 expired_used=0
 obsolete_used=0
 unavailable_used=0

#################################################Fetch Data for SWT2_CPB_LOCALGROUPDISK####################################################################
 SWT2_CPB_LOCALGROUPDISK = wjdata[ 'RSEDATA' ][ 'SWT2_CPB_LOCALGROUPDISK' ]
 for j in SWT2_CPB_LOCALGROUPDISK:
    rse_all.append(j)
 for i in SWT2_CPB_LOCALGROUPDISK:
    if i == 'rucio':
        rucio_used = (SWT2_CPB_LOCALGROUPDISK[ i ][ 'used' ])
        rucio_updated_at = parser.parse(SWT2_CPB_LOCALGROUPDISK[ i ][ 'updated_at' ])
        n = float((float(rucio_used) / int(json_SWT2_CPB_LOCALGROUPDISK)) * 100)
        result7=0
        try:
         result7 = db.rucio_SWT2_CPB_LOCALGROUPDISK.insert_one(
            {
                "updated_at": rucio_updated_at,
                "used": rucio_used
            }
         );
         if(result7):
          if (n > 95):
            mail.mail("Rucio SWT2_CPB_LOCALGROUPDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'json':
        json_used = (SWT2_CPB_LOCALGROUPDISK[ i ][ 'used' ])
        json_updated_at = parser.parse(SWT2_CPB_LOCALGROUPDISK[ i ][ 'updated_at' ])
        n = float((float(json_used) / int(json_SWT2_CPB_LOCALGROUPDISK)) * 100)
        result8=0
        try:
         result8 = db.json_SWT2_CPB_LOCALGROUPDISK.insert_one(
            {
                "updated_at": json_updated_at,
                "used": json_used
            }
         );
         if(result8):
          if (n > 95):
            mail.mail("JSON SWT2_CPB_LOCALGROUPDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
        if (result7 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
            if (result8 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                if ((((rucio_used - json_used) / int(json_SWT2_CPB_LOCALGROUPDISK)) * 100 > 10) or (
                        ((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                    mail.mail("Difference between Rucio and JSON in SWT2_CPB_LOCALGROUPDISK space token is"+str(round((((rucio_used-json_used)/int(json_SWT2_CPB_LOCALGROUPDISK))*100),2))+"% or off by "+((rucio_used-json_used)/1024 / 1024 / 1024 / 1024)+"TB")

    elif i == 'expired':
        expired_used = (SWT2_CPB_LOCALGROUPDISK[ i ][ 'used' ])
        expired_updated_at = parser.parse(SWT2_CPB_LOCALGROUPDISK[ i ][ 'updated_at' ])
        n = float((float(expired_used) /int(json_SWT2_CPB_LOCALGROUPDISK)) * 100)
        result9=0
        try:
         result9 = db.expired_SWT2_CPB_LOCALGROUPDISK.insert_one(
            {
                "updated_at": expired_updated_at,
                "used": expired_used
            }
         );
         if(result9):
          if (n > 95):
            mail.mail("Expired SWT2_CPB_LOCALGROUPDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'unavailable':
        unavailable_used = (SWT2_CPB_LOCALGROUPDISK[ i ][ 'used' ])
        unavailable_updated_at =parser.parse(SWT2_CPB_LOCALGROUPDISK[ i ][ 'updated_at' ])
        n = float((float(unavailable_used) / int(json_SWT2_CPB_LOCALGROUPDISK)) * 100)
        result10=0
        try:
         result10 = db.unavailable_SWT2_CPB_LOCALGROUPDISK.insert_one(
            {
                "updated_at": unavailable_updated_at,
                "used": unavailable_used
            }
         );
         if(result10):
          if (n > 95):
            mail.mail("Unavailable SWT2_CPB_LOCALGROUPDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'gsiftp':
        gsiftp_used = (SWT2_CPB_LOCALGROUPDISK[ i ][ 'used' ])
        gsiftp_updated_at = parser.parse(SWT2_CPB_LOCALGROUPDISK[ i ][ 'updated_at' ])
        n = float((float(gsiftp_used) / int(json_SWT2_CPB_LOCALGROUPDISK)) * 100)
        result11=0
        try:
         result11 = db.gsiftp_SWT2_CPB_LOCALGROUPDISK.insert_one(
            {
                "updated_at": gsiftp_updated_at,
                "used": gsiftp_used
            }
         );
         if(result11):
          if (n > 95):
            mail.mail("GSIFTP SWT2_CPB_LOCALGROUPDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'obsolete':
        obsolete_used = (SWT2_CPB_LOCALGROUPDISK[ i ][ 'used' ])
        obsolete_updated_at=parser.parse(SWT2_CPB_LOCALGROUPDISK[ i ][ 'updated_at' ])
        n = float((float(obsolete_used) / int(json_SWT2_CPB_LOCALGROUPDISK)) * 100)
        result12=0
        try:
         result12 = db.obsolete_SWT2_CPB_LOCALGROUPDISK.insert_one(
            {
                "updated_at": obsolete_updated_at,
                "used": obsolete_used
            }
         );
         if(result12):
          if (n > 95):
            mail.mail("Obsolete SWT2_CPB_LOCALGROUPDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
 rse_all = [ ]
 rucio_used = 0
 json_used = 0
 gsiftp_used = 0
 expired_used = 0
 obsolete_used = 0
 unavailable_used = 0
##################################################Fetch Data for SWT2_CPB_SCRATCHDISK######################################################################
 SWT2_CPB_SCRATCHDISK = wjdata[ 'RSEDATA' ][ 'SWT2_CPB_SCRATCHDISK' ]
 for j in SWT2_CPB_SCRATCHDISK:
    rse_all.append(j)
 for i in SWT2_CPB_SCRATCHDISK:
    if i == 'rucio':
        rucio_used = (SWT2_CPB_SCRATCHDISK[ i ][ 'used' ])
        rucio_updated_at = parser.parse(SWT2_CPB_SCRATCHDISK[ i ][ 'updated_at' ])
        n = float((float(rucio_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100)
        result13=0
        try:
         result13 = db.rucio_SWT2_CPB_SCRATCHDISK.insert_one(
            {
                "updated_at": rucio_updated_at,
                "used": rucio_used
            }
         );
         if(result13):
          if (n > 95):
            mail.mail("Rucio SWT2_CPB_SCRATCHDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'json':
        json_used = (SWT2_CPB_SCRATCHDISK[ i ][ 'used' ])
        json_updated_at = parser.parse(SWT2_CPB_SCRATCHDISK[ i ][ 'updated_at' ])
        n = float((float(json_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100)
        result14=0
        try:
         result14 = db.json_SWT2_CPB_SCRATCHDISK.insert_one(
            {
                "updated_at": json_updated_at,
                "used": json_used
            }
         );
         if(result14):
          if (n > 95):
            mail.mail("JSON SWT2_CPB_SCRATCHDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
        if (result13 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
            if (result14 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                if ((((rucio_used - json_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100 > 10) or (
                        ((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                    mail.mail("Difference between Rucio and JSON in SWT2_CPB_SCRATCHDISK space token is"+str(round((((rucio_used-json_used)/int(json_SWT2_CPB_SCRATCHDISK))*100),2))+"% or off by "+((rucio_used-json_used)/1024 / 1024 / 1024 / 1024)+"TB")

    elif i == 'expired':
        expired_used = (SWT2_CPB_SCRATCHDISK[ i ][ 'used' ])
        expired_updated_at = parser.parse(SWT2_CPB_SCRATCHDISK[ i ][ 'updated_at' ])
        n = float((float(expired_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100)
        result15=0
        try:
         result15 = db.expired_SWT2_CPB_SCRATCHDISK.insert_one(
            {
                "updated_at": expired_updated_at,
                "used": expired_used
            }
         );
         if(result15):
            if (n > 95):
             mail.mail("Expired SWT2_CPB_SCRATCHDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'unavailable':
        unavailable_used = (SWT2_CPB_SCRATCHDISK[ i ][ 'used' ])
        unavailable_updated_at =parser.parse(SWT2_CPB_SCRATCHDISK[ i ][ 'updated_at' ])
        n = float((float(unavailable_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100)
        result16=0
        try:
         result16 = db.unavailable_SWT2_CPB_SCRATCHDISK.insert_one(
            {
                "updated_at": unavailable_updated_at,
                "used": unavailable_used
            }
         );
         if(result16):
          if (n > 95):
            mail.mail("Unavailable SWT2_CPB_SCRATCHDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'gsiftp':
        gsiftp_used = (SWT2_CPB_SCRATCHDISK[ i ][ 'used' ])
        gsiftp_updated_at = parser.parse(SWT2_CPB_SCRATCHDISK[ i ][ 'updated_at' ])
        n = float((float(gsiftp_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100)
        result17=0
        try:
         result17 = db.gsiftp_SWT2_CPB_SCRATCHDISK.insert_one(
            {
                "updated_at": gsiftp_updated_at,
                "used": gsiftp_used
            }
         );
         if(result17):
          if (n > 95):
            mail.mail("GSIFTP SWT2_CPB_SCRATCHDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'obsolete':
        obsolete_used = (SWT2_CPB_SCRATCHDISK[ i ][ 'used' ])
        obsolete_updated_at = parser.parse(SWT2_CPB_SCRATCHDISK[ i ][ 'updated_at' ])
        n = float((float(obsolete_used) / int(json_SWT2_CPB_SCRATCHDISK)) * 100)
        result18=0
        try:
         result18 = db.obsolete_SWT2_CPB_SCRATCHDISK.insert_one(
            {
                "updated_at": obsolete_updated_at,
                "used": obsolete_used
            }
         );
         if(result18):
          if (n > 95):
            mail.mail("Obsolete SWT2_CPB_SCRATCHDISK: " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
 rse_all = [ ]
 rucio_used = 0
 json_used = 0
 gsiftp_used = 0
 expired_used = 0
 obsolete_used = 0
 unavailable_used = 0
#############################################Data for UTA_SWT2_DATADISK######################################################################################


 UTA_SWT2 = wjdata[ 'RSEDATA' ][ 'UTA_SWT2_DATADISK' ]
 for j in UTA_SWT2:
    rse_all.append(j)
 for i in UTA_SWT2:
    if i == 'rucio':
        rucio_used = (UTA_SWT2[ i ][ 'used' ])
        rucio_updated_at = parser.parse(UTA_SWT2[ i ][ 'updated_at' ])
        n = float((float(rucio_used) / int(json_UTA_SWT2_DATADISK)) * 100)
        result19=0
        try:
         result19 = db.rucio_UTA_SWT2.insert_one(
            {
                "updated_at": rucio_updated_at,
                "used": rucio_used
            }
         );
         if(result19):
          if (n > 95):
            mail.mail("UTA_SWT2 Rucio : " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'json':
        json_used = (UTA_SWT2[ i ][ 'used' ])
        json_updated_at = parser.parse(UTA_SWT2[ i ][ 'updated_at' ])
        n = float((float(json_used) / int(json_UTA_SWT2_DATADISK)) * 100)
        result20=0
        try:
         result20 = db.json_UTA_SWT2.insert_one(
            {
                "updated_at": json_updated_at,
                "used": json_used
            }
         );
         if(result20):
          if (n > 95):
            mail.mail("UTA_SWT2 JSON : " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
        if (result19 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
            if (result20 or (((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                if ((((rucio_used - json_used) / int(json_UTA_SWT2_DATADISK)) * 100 > 10) or (
                        ((rucio_used - json_used) / 1024 / 1024 / 1024 / 1024) > int(datadisk_offby))):
                    mail.mail("Difference between Rucio and JSON in SWT2_CPB_SCRATCHDISK space token is"+str(round((((rucio_used-json_used)/int(json_UTA_SWT2_DATADISK))*100),2))+"% or off by "+((rucio_used-json_used)/1024 / 1024 / 1024 / 1024)+"TB")
    elif i == 'expired':
        expired_used = (UTA_SWT2[ i ][ 'used' ])
        expired_updated_at = parser.parse(UTA_SWT2[ i ][ 'updated_at' ])
        n = float((float(expired_used) / int(json_UTA_SWT2_DATADISK)) * 100)
        result21=0
        try:
         result21 = db.expired_UTA_SWT2.insert_one(
            {
                "updated_at": expired_updated_at,
                "used": expired_used
            }
         );
         if(result21):
            if (n > 95):
             mail.mail("UTA_SWT2 Expired : " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'unavailable':
        unavailable_used = (UTA_SWT2[ i ][ 'used' ])
        unavailable_updated_at =parser.parse(UTA_SWT2[ i ][ 'updated_at' ])
        n = float((float(unavailable_used) / int(json_UTA_SWT2_DATADISK)) * 100)
        result22=0
        try:
         result22 = db.unavailable_UTA_SWT2.insert_one(
            {
                "updated_at": unavailable_updated_at,
                "used": unavailable_used
            }
         );
         if(result22):
          if (n > 95):
            mail.mail("UTA_SWT2 Unavailable : " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass


    elif i == 'gsiftp':
        gsiftp_used = (UTA_SWT2[ i ][ 'used' ])
        gsiftp_updated_at = parser.parse(UTA_SWT2[ i ][ 'updated_at' ])
        n = float((float(gsiftp_used) / int(json_UTA_SWT2_DATADISK)) * 100)
        result23=0
        try:
         result23 = db.gsiftp_UTA_SWT2.insert_one(
            {
                "updated_at": gsiftp_updated_at,
                "used": gsiftp_used
            }
         );
         if(result23):
          if (n > 95):
            mail.mail("UTA_SWT2 GSIFTP : " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
    elif i == 'obsolete':
        obsolete_used = (UTA_SWT2[ i ][ 'used' ])
        obsolete_updated_at = parser.parse(UTA_SWT2[ i ][ 'updated_at' ])
        n = float((float(obsolete_used) / int(json_UTA_SWT2_DATADISK)) * 100)
        result24=0
        try:
         result24 = db.obsolete_UTA_SWT2.insert_one(
            {
                "updated_at": obsolete_updated_at,
                "used": obsolete_used
            }
         );
         if(result24):
           if (n > 95):
            mail.mail("UTA_SWT2 Obsolete : " + str(round(n,2)) + "%")
        except pymongo.errors.DuplicateKeyError:
            pass
