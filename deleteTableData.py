from pymongo import MongoClient
import pymongo
from datetime import datetime
from dateutil.relativedelta import relativedelta


client = MongoClient('mongodb://axr6305:secretPassword@localhost:27017/mydata')
#client = MongoClient()
db=client['mydata']
x = datetime.now() - relativedelta(years=1)


###################################################Deletion Tables########################################################
db.del_SWT2_CPB.find({}).sort("to_date", pymongo.ASCENDING)
db.del_SWT2_CPB.delete_many({"to_date":{"$lte": x}})


db.del_UTA_SWT2.find({}).sort("to_date", pymongo.ASCENDING)
db.del_UTA_SWT2.delete_many({"to_date":{"$lte": x}})

db.del_OU_OSCER_ATLAS.find({}).sort("to_date", pymongo.ASCENDING)
db.del_OU_OSCER_ATLAS.delete_many({"to_date":{"$lte": x}})

db.del_LUCILLE.find({}).sort("to_date", pymongo.ASCENDING)
db.del_LUCILLE.delete_many({"to_date":{"$lte": x}})


##########################################################Storage Tables#################################################################
#rucio_SWT2_CPB_DATADISK


db.rucio_SWT2_CPB_DATADISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.rucio_SWT2_CPB_DATADISK.delete_many({"updated_at":{"$lte": x}})

#json_SWT2_CPB_DATADISK


db.json_SWT2_CPB_DATADISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.json_SWT2_CPB_DATADISK.delete_many({"updated_at":{"$lte": x}})

#expired_SWT2_CPB_DATADISK


db.expired_SWT2_CPB_DATADISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.expired_SWT2_CPB_DATADISK.delete_many({"updated_at":{"$lte": x}})

#unavailable_SWT2_CPB_DATADISK


db.unavailable_SWT2_CPB_DATADISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.unavailable_SWT2_CPB_DATADISK.delete_many({"updated_at":{"$lte": x}})

#gsiftp_SWT2_CPB_DATADISK


db.gsiftp_SWT2_CPB_DATADISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.gsiftp_SWT2_CPB_DATADISK.delete_many({"updated_at":{"$lte": x}})

#obsolete_SWT2_CPB_DATADISK


db.obsolete_SWT2_CPB_DATADISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.obsolete_SWT2_CPB_DATADISK.delete_many({"updated_at":{"$lte": x}})

#rucio_SWT2_CPB_LOCALGROUPDISK


db.rucio_SWT2_CPB_LOCALGROUPDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.rucio_SWT2_CPB_LOCALGROUPDISK.delete_many({"updated_at":{"$lte": x}})

#json_SWT2_CPB_LOCALGROUPDISK


db.json_SWT2_CPB_LOCALGROUPDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.json_SWT2_CPB_LOCALGROUPDISK.delete_many({"updated_at":{"$lte": x}})


#expired_SWT2_CPB_LOCALGROUPDISK


db.expired_SWT2_CPB_LOCALGROUPDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.expired_SWT2_CPB_LOCALGROUPDISK.delete_many({"updated_at":{"$lte": x}})

#unavailable_SWT2_CPB_LOCALGROUPDISK


db.unavailable_SWT2_CPB_LOCALGROUPDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.unavailable_SWT2_CPB_LOCALGROUPDISK.delete_many({"updated_at":{"$lte": x}})

#gsiftp_SWT2_CPB_LOCALGROUPDISK


db.gsiftp_SWT2_CPB_LOCALGROUPDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.gsiftp_SWT2_CPB_LOCALGROUPDISK.delete_many({"updated_at":{"$lte": x}})

#obsolete_SWT2_CPB_LOCALGROUPDISK


db.obsolete_SWT2_CPB_LOCALGROUPDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.obsolete_SWT2_CPB_LOCALGROUPDISK.delete_many({"updated_at":{"$lte": x}})

#rucio_SWT2_CPB_SCRATCHDISK


db.rucio_SWT2_CPB_SCRATCHDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.rucio_SWT2_CPB_SCRATCHDISK.delete_many({"updated_at":{"$lte": x}})

#json_SWT2_CPB_SCRATCHDISK


db.json_SWT2_CPB_SCRATCHDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.json_SWT2_CPB_SCRATCHDISK.delete_many({"updated_at":{"$lte": x}})

#expired_SWT2_CPB_SCRATCHDISK


db.expired_SWT2_CPB_SCRATCHDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.expired_SWT2_CPB_SCRATCHDISK.delete_many({"updated_at":{"$lte": x}})

#unavailable_SWT2_CPB_SCRATCHDISK


db.unavailable_SWT2_CPB_SCRATCHDISK.find({}).sort("to_date", pymongo.ASCENDING)
db.unavailable_SWT2_CPB_SCRATCHDISK.delete_many({"to_date":{"$lte": x}})

#gsiftp_SWT2_CPB_SCRATCHDISK


db.gsiftp_SWT2_CPB_SCRATCHDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.gsiftp_SWT2_CPB_SCRATCHDISK.delete_many({"updated_at":{"$lte": x}})

#obsolete_SWT2_CPB_SCRATCHDISK


db.obsolete_SWT2_CPB_SCRATCHDISK.find({}).sort("updated_at", pymongo.ASCENDING)
db.obsolete_SWT2_CPB_SCRATCHDISK.delete_many({"updated_at":{"$lte": x}})

#rucio_UTA_SWT2


db.rucio_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
db.rucio_UTA_SWT2.delete_many({"updated_at":{"$lte": x}})

#json_UTA_SWT2


db.json_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
db.json_UTA_SWT2.delete_many({"updated_at":{"$lte": x}})

#expired_UTA_SWT2


db.expired_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
db.expired_UTA_SWT2.delete_many({"updated_at":{"$lte": x}})

#unavailable_UTA_SWT2


db.unavailable_UTA_SWT2.find({}).sort("to_date", pymongo.ASCENDING)
db.unavailable_UTA_SWT2.delete_many({"to_date":{"$lte": x}})

#gsiftp_UTA_SWT2


db.gsiftp_UTA_SWT2.find({}).sort("to_date", pymongo.ASCENDING)
db.gsiftp_UTA_SWT2.delete_many({"to_date":{"$lte": x}})

#obsolete_UTA_SWT2


db.obsolete_UTA_SWT2.find({}).sort("updated_at", pymongo.ASCENDING)
db.obsolete_UTA_SWT2.delete_many({"updated_at":{"$lte": x}})


##########################################################Transfer Tables#################################################################

db.Transfer_Tables_UTA_Dest.find({}).sort("to_date", pymongo.ASCENDING)
db.Transfer_Tables_UTA_Dest.delete_many({"to_date":{"$lte": x}})


db.Transfer_Tables_UTA_Src.find({}).sort("to_date", pymongo.ASCENDING)
db.Transfer_Tables_UTA_Src.delete_many({"to_date":{"$lte": x}})






