from flask import Flask, render_template,request
import SWT2_CPB_DATADISK as d
import SWT2_CPB_SCRATCHDISK as a
import SWT2_CPB_LOCALGROUPDISK as b
import UTA_SWT2_DATADISK as c
import slider as s
import Deletion as e
import Transfer_UTA_Dest as t
import Transfer_UTA_Src as u
import transferFunction
from pymongo import MongoClient
import ConfigParser,os
import slider as s


client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']

dirname=os.getcwd()
#dirname = os.path.dirname(__file__)
filename = dirname + '/config.cfg'
Config = ConfigParser.ConfigParser()
Config.read(filename)
for x in db.json_total.find({"space_token":'json_SWT2_CPB_DATADISK'}):
 json_SWT2_CPB_DATADISK =x["total"]
for x in db.json_total.find({"space_token":'json_SWT2_CPB_LOCALGROUPDISK'}):
 json_SWT2_CPB_LOCALGROUPDISK =x["total"]
for x in db.json_total.find({"space_token":'json_SWT2_CPB_SCRATCHDISK'}):
 json_SWT2_CPB_SCRATCHDISK =x["total"]
for x in db.json_total.find({"space_token":'json_UTA_SWT2_DATADISK'}):
 json_UTA_SWT2_DATADISK =x["total"]

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
   list_Swt2CpbDATADISK = d.Swt2CpbDATADISK().data_prep()[ 0 ]
   list_Swt2CpbLOCALGRPDISK = b.Swt2CpbLOCALGRPDISK().data_prep()[ 0 ]
   list_Swt2CpbSCRATCHDISK = a.Swt2CpbSCRATCHDISK().data_prep()[ 0 ]
   list_utaswt2 = c.utaswt2().data_prep()[ 0 ]

   return render_template('index.html', list=list_Swt2CpbDATADISK,list_local=list_Swt2CpbLOCALGRPDISK,list_scratch=list_Swt2CpbSCRATCHDISK,uta_data=list_utaswt2,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK,json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK,json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK,json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK)

#####################################################################Slider##########################################################################
# def readDays():
#     for x in db.appConfig.find({'key': 'day_365'}, {"key": 1, "value": 1, "_id": 0}):  # 1
#         l=x['value']
#     return l

@app.route('/slider')
def slider():
   lv =s.read.readDays()
   return render_template('slider.html', l=lv)
@app.route('/updateSlider', methods=['POST'])
def updateSlider():
    vDays =  request.form['vDays'];
    # saving the updated value into DB
    db.appConfig.update_many({
        'key': 'day_365'
    }, {
        '$set': {
            'value': int(vDays)
        }
    }, upsert=False)
    return "success";


#######################################################################################################################################################

@app.route('/SWT2_CPB_DATADISK')
def SWT2_CPB_DATADISK():
   list=d.Swt2CpbDATADISK.data_prep()[0]
   return render_template('SWT2_CPB_DATADISK_View.html', list=list,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK, rucio7=d.Swt2CpbDATADISK.rucio7, expired7=d.Swt2CpbDATADISK.expired7, gsiftp7=d.Swt2CpbDATADISK.gsiftp7,
                          obsolete7=d.Swt2CpbDATADISK.obsolete7, json7=d.Swt2CpbDATADISK.json7, unavailable7=d.Swt2CpbDATADISK.unavailable7)


@app.route('/SWT2_CPB_SCRATCHDISK',methods=['GET','POST'])
def SWT2_CPB_SCRATCHDISK():
   list=a.Swt2CpbSCRATCHDISK.data_prep()[0]
   return render_template('SWT2_CPB_SCRATCHDISK_View.html', list=list,json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, rucio7=a.Swt2CpbSCRATCHDISK.rucio7, expired7=a.Swt2CpbSCRATCHDISK.expired7, gsiftp7=a.Swt2CpbSCRATCHDISK.gsiftp7,
                          obsolete7=a.Swt2CpbSCRATCHDISK.obsolete7, json7=a.Swt2CpbSCRATCHDISK.json7, unavailable7=a.Swt2CpbSCRATCHDISK.unavailable7)

@app.route('/SWT2_CPB_LOCALGROUPDISK',methods=['GET','POST'])
def SWT2_CPB_LOCALGROUPDISK():
   list=b.Swt2CpbLOCALGRPDISK.data_prep()[0]
   return render_template('SWT2_CPB_LOCALGROUPDISK_View.html', list=list,json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, rucio7=b.Swt2CpbLOCALGRPDISK.rucio7, expired7=b.Swt2CpbLOCALGRPDISK.expired7, gsiftp7=b.Swt2CpbLOCALGRPDISK.gsiftp7,
                          obsolete7=b.Swt2CpbLOCALGRPDISK.obsolete7, json7=b.Swt2CpbLOCALGRPDISK.json7, unavailable7=b.Swt2CpbLOCALGRPDISK.unavailable7)


@app.route('/UTA_SWT2_DATAPDISK',methods=['GET','POST'])
def UTA_SWT2_DATAPDISK():
   list=c.utaswt2.data_prep()[0]
   return render_template('UTA_SWT2_DATADISK_View.html', list=list,json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK, rucio7=c.utaswt2.ruciox_7, expired7=c.utaswt2.expiredx_7, gsiftp7=c.utaswt2.gsiftpx_7,
                          obsolete7=c.utaswt2.expiredx_7, json7=c.utaswt2.jsonx_7, unavailable7=c.utaswt2.unavailablex_7)
# ##########################################################Data Disk##########################################################

@app.route('/Rucio',methods=['GET','POST'])
def Rucio():
 rucio_json = d.Swt2CpbDATADISK.data_prep()[1]
 return render_template('rucioDetail.html', rucio_json=rucio_json,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK)

@app.route('/JSON',methods=['GET','POST'])
def JSON():
 jsonx_json = d.Swt2CpbDATADISK.data_prep()[5]
 return render_template('jsonDetail.html', jsonx_json=jsonx_json,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK)

@app.route('/GSIFTP',methods=['GET','POST'])
def GSIFTP():
 gsiftp_json = d.Swt2CpbDATADISK.data_prep()[3]
 return render_template('gsiftpDetail.html', gsiftp_json=gsiftp_json,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK)

@app.route('/Expired',methods=['GET','POST'])
def Expired():
  expired_json = d.Swt2CpbDATADISK.data_prep()[2]
  return render_template('expiredDetail.html', expired_json=expired_json,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK)

@app.route('/Obsolete',methods=['GET','POST'])
def Obsolete():
  obsolete_json= d.Swt2CpbDATADISK.data_prep()[4]
  return render_template('obsoleteDetail.html', obsolete_json=obsolete_json,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK)

@app.route('/Unaivalable',methods=['GET','POST'])
def Unaivalable():
  unavailable_json = d.Swt2CpbDATADISK.data_prep()[6]
  return render_template('unavailableDetail.html', unavailable_json=unavailable_json,json_SWT2_CPB_DATADISK=json_SWT2_CPB_DATADISK)

#############################################################Deletion Main Page##########################################################

@app.route('/Deletion', methods=['GET','POST'])
def Deletion():
  return render_template('Deletion.html')


############################################################Deletion swt2_cpb############################################################

@app.route('/DeletionSWT2CPB', methods=['GET','POST'])
def DeletionSWT2CPB():
  list=e.Del.data_prep_swt2_cpb()[0]
  planned_bytes_yr=e.Del.data_prep_swt2_cpb()[1]
  failed_bytes_yr=e.Del.data_prep_swt2_cpb()[2]
  done_bytes_yr=e.Del.data_prep_swt2_cpb()[3]
  planned_files_yr=e.Del.data_prep_swt2_cpb()[4]
  failed_files_yr=e.Del.data_prep_swt2_cpb()[5]
  done_files_yr=e.Del.data_prep_swt2_cpb()[6]
  return render_template('Deletion_SWT2_CPB.html', list=list, planned_bytes=e.Del.planned_bytes_swt2_cpb, failed_bytes=e.Del.failed_bytes_swt2_cpb,
                         done_bytes=e.Del.done_bytes_swt2_cpb,planned_files=e.Del.planned_files_swt2_cpb,failed_files=e.Del.failed_files_swt2_cpb,done_files=e.Del.done_files_swt2_cpb,
                         planned_bytes_yr=planned_bytes_yr, failed_bytes_yr=failed_bytes_yr, done_bytes_yr=done_bytes_yr,
                         planned_files_yr=planned_files_yr,failed_files_yr=failed_files_yr,done_files_yr=done_files_yr)

@app.route('/DeletionPlannedBytes')
def DeletionPlannedBytes_swt2cpb():
    planned_bytes_yr = e.Del.data_prep_swt2_cpb()[ 1 ]
    return render_template('deletionPlannedBytes_SWT2_CPB.html', planned_bytes_yr=planned_bytes_yr)


@app.route('/DeletionFailedBytes')
def DeletionFailedBytes_swt2cpb():
    failed_bytes_yr = e.Del.data_prep_swt2_cpb()[ 2 ]
    return render_template('deletionFailedBytes_SWT2_CPB.html', failed_bytes_yr=failed_bytes_yr)


@app.route('/DeletionDoneBytes')
def DeletionDoneBytes_swt2cpb():
    done_bytes_yr = e.Del.data_prep_swt2_cpb()[ 3 ]
    return render_template('deletionDoneBytes_SWT2_CPB.html', done_bytes_yr=done_bytes_yr)


@app.route('/DeletionPlannedFiles')
def DeletionPlannedFiles_swt2cpb():
    planned_files_yr = e.Del.data_prep_swt2_cpb()[ 4 ]
    return render_template('deletionPlannedFiles_SWT2_CPB.html', planned_files_yr=planned_files_yr)

@app.route('/DeletionFailedFiles')
def DeletionFailedFiles_swt2cpb():
    failed_files_yr = e.Del.data_prep_swt2_cpb()[ 5 ]
    return render_template('deletionFailedFiles_SWT2_CPB.html', failed_files_yr=failed_files_yr)

@app.route('/DeletionDoneFiles')
def DeletionDoneFiles_swt2cpb():
    done_files_yr = e.Del.data_prep_swt2_cpb()[ 6 ]
    return render_template('deletionDoneFiles_SWT2_CPB.html', done_files_yr=done_files_yr)


#####################################################Deletion UTA SWT2##########################################################################


@app.route('/DeletionUTASWT2', methods=['GET','POST'])
def DeletionUTASWT2():
  list=e.Del.data_prep_uta_swt2()[0]
  planned_bytes_yr=e.Del.data_prep_uta_swt2()[1]
  failed_bytes_yr=e.Del.data_prep_uta_swt2()[2]
  done_bytes_yr=e.Del.data_prep_uta_swt2()[3]
  planned_files_yr=e.Del.data_prep_uta_swt2()[4]
  failed_files_yr=e.Del.data_prep_uta_swt2()[5]
  done_files_yr=e.Del.data_prep_uta_swt2()[6]
  return render_template('Deletion_UTA_SWT2.html', list=list, planned_bytes=e.Del.planned_bytes_uta_swt2, failed_bytes=e.Del.failed_bytes_uta_swt2,
                         done_bytes=e.Del.done_bytes_uta_swt2 ,planned_files=e.Del.planned_files_uta_swt2,failed_files=e.Del.failed_files_uta_swt2,done_files=e.Del.done_files_uta_swt2,
                         planned_bytes_yr=planned_bytes_yr, failed_bytes_yr=failed_bytes_yr, done_bytes_yr=done_bytes_yr,
                         planned_files_yr=planned_files_yr,failed_files_yr=failed_files_yr,done_files_yr=done_files_yr)


@app.route('/DeletionPlannedBytesUTASWT2')
def DeletionPlannedBytes_utaswt2():
    planned_bytes_yr = e.Del.data_prep_uta_swt2()[ 1 ]
    return render_template('deletionPlannedBytes_UTA_SWT2.html', planned_bytes_yr=planned_bytes_yr)


@app.route('/DeletionFailedBytesUTASWT2')
def DeletionFailedBytes_utaswt2():
    failed_bytes_yr = e.Del.data_prep_uta_swt2()[ 2 ]
    return render_template('deletionFailedBytes_UTA_SWT2.html', failed_bytes_yr=failed_bytes_yr)


@app.route('/DeletionDoneBytesUTASWT2')
def DeletionDoneBytes_utaswt2():
    done_bytes_yr = e.Del.data_prep_uta_swt2()[ 3 ]
    return render_template('deletionDoneBytes_UTA_SWT2.html', done_bytes_yr=done_bytes_yr)

@app.route('/DeletionPlannedFilesUTASWT2')
def DeletionPlannedFiles_utaswt2():
    planned_files_yr = e.Del.data_prep_uta_swt2()[ 4 ]
    return render_template('deletionPlannedFiles_UTA_SWT2.html', planned_files_yr=planned_files_yr)

@app.route('/DeletionFailedFilesUTASWT2')
def DeletionFailedFiles_utaswt2():
    failed_files_yr = e.Del.data_prep_uta_swt2()[ 5 ]
    return render_template('deletionFailedFiles_UTA_SWT2.html', failed_files_yr=failed_files_yr)

@app.route('/DeletionDoneFilesUTASWT2')
def DeletionDoneFiles_utaswt2():
    done_files_yr = e.Del.data_prep_uta_swt2()[ 6 ]
    return render_template('deletionDoneFiles_UTA_SWT2.html', done_files_yr=done_files_yr)

#########################################################Deletion OU OSCER######################################################################
@app.route('/DeletionOUOSCER', methods=['GET','POST'])
def DeletionOUOSCER():
  list=e.Del.data_prep_ou_oscer()[0]
  planned_bytes_yr=e.Del.data_prep_ou_oscer()[1]
  failed_bytes_yr=e.Del.data_prep_ou_oscer()[2]
  done_bytes_yr=e.Del.data_prep_ou_oscer()[3]
  planned_files_yr=e.Del.data_prep_ou_oscer()[4]
  failed_files_yr=e.Del.data_prep_ou_oscer()[5]
  done_files_yr=e.Del.data_prep_ou_oscer()[6]
  return render_template('Deletion_OU_OSCER.html', list=list, planned_bytes=e.Del.planned_bytes_ou_oscer, failed_bytes=e.Del.failed_bytes_ou_oscer,
                         done_bytes=e.Del.done_bytes_ou_oscer,planned_files=e.Del.planned_files_ou_oscer,failed_files=e.Del.failed_files_ou_oscer,done_files=e.Del.done_files_ou_oscer,
                         planned_bytes_yr=planned_bytes_yr, failed_bytes_yr=failed_bytes_yr, done_bytes_yr=done_bytes_yr,
                         planned_files_yr=planned_files_yr,failed_files_yr=failed_files_yr,done_files_yr=done_files_yr)

@app.route('/DeletionPlannedBytesOSCER')
def DeletionPlannedBytesOSCER():
    planned_bytes_yr = e.Del.data_prep_ou_oscer()[ 1 ]
    return render_template('deletionPlannedBytes_OU_OSCER.html', planned_bytes_yr=planned_bytes_yr)


@app.route('/DeletionFailedBytesOSCER')
def DeletionFailedBytesOSCER():
    failed_bytes_yr = e.Del.data_prep_ou_oscer()[ 2 ]
    return render_template('deletionFailedBytes_OU_OSCER.html', failed_bytes_yr=failed_bytes_yr)


@app.route('/DeletionDoneBytesOSCER')
def DeletionDoneBytesOSCER():
    done_bytes_yr = e.Del.data_prep_ou_oscer()[ 3 ]
    return render_template('deletionDoneBytes_OU_OSCER.html', done_bytes_yr=done_bytes_yr)


@app.route('/DeletionPlannedFilesOSCER')
def DeletionPlannedFilesOSCER():
    planned_files_yr = e.Del.data_prep_ou_oscer()[ 4 ]
    return render_template('deletionPlannedFiles_OU_OSCER.html', planned_files_yr=planned_files_yr)

@app.route('/DeletionFailedFilesOSCER')
def DeletionFailedFilesOSCER():
    failed_files_yr = e.Del.data_prep_ou_oscer()[ 5 ]
    return render_template('deletionFailedFiles_OU_OSCER.html', failed_files_yr=failed_files_yr)

@app.route('/DeletionDoneFilesOSCER')
def DeletionDoneFilesOSCER():
    done_files_yr = e.Del.data_prep_ou_oscer()[ 6 ]
    return render_template('deletionDoneFiles_OU_OSCER.html', done_files_yr=done_files_yr)

#####################################################Deletion LUCCILE#########################################################################
@app.route('/DeletionLUCCILE', methods=['GET','POST'])
def DeletionLUCCILE():
  list=e.Del.data_prep_lucille()[0]
  planned_bytes_yr=e.Del.data_prep_lucille()[1]
  failed_bytes_yr=e.Del.data_prep_lucille()[2]
  done_bytes_yr=e.Del.data_prep_lucille()[3]
  planned_files_yr=e.Del.data_prep_lucille()[4]
  failed_files_yr=e.Del.data_prep_lucille()[5]
  done_files_yr=e.Del.data_prep_lucille()[6]
  return render_template('Deletion_LUCCILE.html', list=list, planned_bytes=e.Del.planned_bytes_luccile, failed_bytes=e.Del.failed_bytes_luccile,
                         done_bytes=e.Del.done_bytes_luccile ,planned_files=e.Del.planned_files_luccile,failed_files=e.Del.failed_files_luccile,done_files=e.Del.done_files_luccile,
                         planned_bytes_yr=planned_bytes_yr, failed_bytes_yr=failed_bytes_yr, done_bytes_yr=done_bytes_yr,
                         planned_files_yr=planned_files_yr,failed_files_yr=failed_files_yr,done_files_yr=done_files_yr)

@app.route('/DeletionPlannedBytesLUCCILE')
def DeletionPlannedBytesLUCCILE():
    planned_bytes_yr = e.Del.data_prep_lucille()[ 1 ]
    return render_template('deletionPlannedBytes_LUCCILE.html', planned_bytes_yr=planned_bytes_yr)


@app.route('/DeletionFailedBytesLUCCILE')
def DeletionFailedBytesLUCCILE():
    failed_bytes_yr = e.Del.data_prep_lucille()[ 2 ]
    return render_template('deletionFailedBytes_LUCCILE.html', failed_bytes_yr=failed_bytes_yr)


@app.route('/DeletionDoneBytesLUCCILE')
def DeletionDoneBytesLUCCILE():
    done_bytes_yr = e.Del.data_prep_lucille()[ 3 ]
    return render_template('deletionDoneBytes_LUCCILE.html', done_bytes_yr=done_bytes_yr)

@app.route('/DeletionPlannedFilesLUCCILE')
def DeletionPlannedFilesLUCCILE():
    planned_files_yr = e.Del.data_prep_lucille()[ 4 ]
    return render_template('deletionPlannedFiles_LUCCILE.html', planned_files_yr=planned_files_yr)

@app.route('/DeletionFailedFilesLUCCILE')
def DeletionFailedFilesLUCCILE():
    failed_files_yr = e.Del.data_prep_lucille()[ 5 ]
    return render_template('deletionFailedFiles_LUCCILE.html', failed_files_yr=failed_files_yr)

@app.route('/DeletionDoneFilesLUCCILE')
def DeletionDoneFilesLUCCILE():
    done_files_yr = e.Del.data_prep_lucille()[ 6 ]
    return render_template('deletionDoneFiles_LUCCILE.html', done_files_yr=done_files_yr)

#########################################################Transfer#####################################################################

@app.route('/Transfer',methods=['GET','POST'])
def Tran():
    return render_template('Transfer.html')

@app.route('/TransferSWT2Destination',methods=['GET','POST'])
def Transfer():
  return render_template('Gridview_UTA_Dest.html', data=t.Transfer_UTA_Dest.data1)

@app.route('/TransferDetail',methods=['GET','POST'])
def TransferDetail():
  data=request.args.get("input")
  dst=data.split("^")[0]
  src=data.split("^")[1]
  x=transferFunction.transferFunction()
  bytes=x.createData(dst,src)
  files=x.createData1(dst,src)
  failures=x.createData3(dst,src)
  prcnt=x.createData4(dst,src)
  return render_template('Transfer_Detail.html',chart1= bytes,chart2=files,chart3=failures,chart4=prcnt,a=src,b=dst)


@app.route('/TransferSWT2Source',methods=['GET','POST'])
def TransferSWT2Source():
  return render_template('Gridview_UTA_Src.html', data=u.Transfer_UTA_Src.data1)

@app.route('/TransferDetailSWT2Src',methods=['GET','POST'])
def TransferDetailSWT2Src():
   data=request.args.get("input")
   dst=data.split("^")[0]
   src=data.split("^")[1]
   x=transferFunction.transferFunction()
   bytes=x.createData(dst,src)
   files=x.createData1(dst,src)
   failures=x.createData3(dst,src)
   prcnt=x.createData4(dst,src)
   return render_template('Transfer_Detail.html', chart1= bytes,chart2=files,chart3=failures,chart4=prcnt,a=dst,b=src)

###########################################################Scratch Disk##########################################################
@app.route('/Rucio_Scratchdisk',methods=['GET','POST'])
def Rucio_Scratchdisk():
  rucio_json = a.Swt2CpbSCRATCHDISK.data_prep()[1]
  return render_template('rucioDetail_SCRATCHDISK.html',json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, rucio_json=rucio_json)

@app.route('/Json_Scratchdisk',methods=['GET','POST'])
def Json_Scratchdisk():
  jsonx_json = a.Swt2CpbSCRATCHDISK.data_prep()[5]
  return render_template('jsonDetail_SCRATCHDISK.html',json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, jsonx_json=jsonx_json)

@app.route('/GSIFTP_Scratchdisk',methods=['GET','POST'])
def GSIFTP_Scratchdisk():
  gsiftp_json = a.Swt2CpbSCRATCHDISK.data_prep()[3]
  return render_template('gsiftpDetail_SCRATCHDISK.html',json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, gsiftp_json=gsiftp_json)

@app.route('/Expired_Scratchdisk',methods=['GET','POST'])
def Expired_Scratchdisk():
  expired_json = a.Swt2CpbSCRATCHDISK.data_prep()[2]
  return render_template('expiredDetail_SCRATCHDISK.html',json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, expired_json=expired_json)

@app.route('/Obsolete_Scratchdisk',methods=['GET','POST'])
def Obsolete_Scratchdisk():
  obsolete_json = a.Swt2CpbSCRATCHDISK.data_prep()[4]
  return render_template('obsoleteDetail_SCRATCHDISK.html',json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, obsolete_json=obsolete_json)

@app.route('/Unaivalable_Scratchdisk',methods=['GET','POST'])
def Unaivalable_Scratchdisk():
  unavailable_json = a.Swt2CpbSCRATCHDISK.data_prep()[6]
  return render_template('unaivalableDetail_SCRATCHDISK.html',json_SWT2_CPB_SCRATCHDISK=json_SWT2_CPB_SCRATCHDISK, unavailable_json=unavailable_json)


# ##########################################################Local Group Disk##########################################################
@app.route('/Rucio_LocalGrpdisk',methods=['GET','POST'])
def Rucio_LocalGrpdisk():
  rucio_json = b.Swt2CpbLOCALGRPDISK.data_prep()[1]
  return render_template('rucioDetail_LOCALGRPDISK.html',json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, rucio_json=rucio_json)

@app.route('/Json_LocalGrpdisk',methods=['GET','POST'])
def Json_LocalGrpdisk():
  jsonx_json = b.Swt2CpbLOCALGRPDISK.data_prep()[5]
  return render_template('jsonDetail_LOCALGRPDISK.html',json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, jsonx_json=jsonx_json)

@app.route('/GSIFTP_LocalGrpdisk',methods=['GET','POST'])
def GSIFTP_LocalGrpdisk():
  gsiftp_json = b.Swt2CpbLOCALGRPDISK.data_prep()[3]
  return render_template('gsiftpDetail_LOCALGRPDISK.html',json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, gsiftp_json=gsiftp_json)

@app.route('/Expired_LocalGrpdisk',methods=['GET','POST'])
def Expired_LocalGrpdisk():
  expired_json= b.Swt2CpbLOCALGRPDISK.data_prep()[2]
  return render_template('expiredDetail_LOCALGRPDISK.html',json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, expired_json=expired_json)

@app.route('/Obsolete_LocalGrpdisk',methods=['GET','POST'])
def Obsolete_LocalGrpdisk():
  obsolete_json = b.Swt2CpbLOCALGRPDISK.data_prep()[4]
  return render_template('obsoleteDetail_LOCALGRPDISK.html',json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, obsolete_json=obsolete_json)

@app.route('/Unaivalable_LocalGrpdisk',methods=['GET','POST'])
def Unaivalable_LocalGrpdisk():
  unavailable_json = b.Swt2CpbLOCALGRPDISK.data_prep()[6]
  return render_template('unaivalableDetail_LOCALGRPDISK.html',json_SWT2_CPB_LOCALGROUPDISK=json_SWT2_CPB_LOCALGROUPDISK, unavailable_json=unavailable_json)


# ##########################################################UTA Data Disk##########################################################
@app.route('/rucioUTA',methods=['GET','POST'])
def rucioUTA():
    rucio_yr = c.utaswt2.data_prep()[1]
    return render_template('rucioDetail_UTA.html',json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK, rucio_json=rucio_yr)

@app.route('/jsonUTA',methods=['GET','POST'])
def jsonUTA():
    json_yr = c.utaswt2.data_prep()[5]
    return render_template('jsonDetail_UTA.html',json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK, jsonx_json=json_yr)

@app.route('/gsiftpUTA',methods=['GET','POST'])
def gsiftpUTA():
    gsiftp_yr = c.utaswt2.data_prep()[3]
    return render_template('gsiftpDetail_UTA.html',json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK,gsiftp_json=gsiftp_yr)

@app.route('/expiredUTA',methods=['GET','POST'])
def expiredUTA():
    expired_yr = c.utaswt2.data_prep()[2]
    return render_template('expiredDetail_UTA.html',json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK,expired_json=expired_yr)

@app.route('/obsoleteUTA',methods=['GET','POST'])
def obsoleteUTA():
    obsolete_yr = c.utaswt2.data_prep()[4]
    return render_template('obsoleteDetail_UTA.html',json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK,obsolete_json=obsolete_yr)

@app.route('/unavailableUTA',methods=['GET','POST'])
def unavailableUTA():
    unavailable_yr = c.utaswt2.data_prep()[6]
    return render_template('unavailableDetail_UTA.html',json_UTA_SWT2_DATADISK=json_UTA_SWT2_DATADISK,unavailable_json=unavailable_yr)

# ####################################################################################################################


@app.errorhandler(404)
def page_not_found(e):
  return  render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
      return  render_template('500.html'), 500
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host="0.0.0.0",port=5000)
