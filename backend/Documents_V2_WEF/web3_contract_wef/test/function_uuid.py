#import time
import contract_inst_uuid_gas
#import contract_inst_uuid_nogas

def Checkuuid():
    global uuid
    uuid=contract_inst_uuid_gas.retrive_useruuid()
    #value = ret_val
    #return ret_val

Checkuuid()
print (uuid)
#use crontab to exute the project time.sleep(600)
