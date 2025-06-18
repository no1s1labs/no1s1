############################
from web3 import Web3,HTTPProvider
from web3.auto import w3
from no1s1AppAddress import AppAddress
from no1s1DataAddress import DataAddress
import json
import time
######################

from defaultaccount import account
from encode import key
from iot.__init__parser import main_parser


################################
with open("./no1s1App.json") as na:
  AppAbi=json.load(na)

with open("./no1s1Data.json") as da:
  DataAbi=json.load(da)
  

w3=Web3(HTTPProvider('https://rinkeby.infura.io/v3/d71645cb22754ded9d58d9b6b4006424'))
AppContract=w3.eth.contract(address = AppAddress, abi=AppAbi)
AppContract.address = AppAddress
DataContract=w3.eth.contract(address = DataAddress, abi=DataAbi)
DataContract.address = DataAddress
print(w3.eth.block_number)

#event_filter=DataContract.eventFilter('newQRcode',{'fromBLock': 0,'toBlock':'latest'})

#w3.eth.getTransactionReceipt(txhash)
event_newuser = DataContract.events.newQRcode.createFilter(fromBlock=0)
allevent_newuser=event_newuser.get_all_entries()
event_authcontract= DataContract.events.AuthorizedContract.createFilter(fromBlock=0)
allevent_authcontract=event_authcontract.get_all_entries()
###############################################################

def broadcastData(Bcurrent,Bvoltage,BSOC,Pvoltage,Senergy,Time):
  nonce = w3.eth.getTransactionCount(account)

    #Calling the newReading function of contract to log readings
  txn_dict = AppContract.functions.broadcastData(Bcurrent,Bvoltage,BSOC,Pvoltage,Senergy,Time).buildTransaction({
        'chainId': 4,
        'gas': 46000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

  #signing the transaction 
  signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = key)
  txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
  txn_receipt = None
  #check if the transaction happened and return the txhash
  while txn_receipt is None:
      txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
      print(txn_receipt)
      #time.sleep(10)
      #value=txn_receipt.logs[0]['data']
      #d_val=int(value,16)
      #print(d_val)
      return txn_receipt

  if txn_receipt is None:
      return {'status': 'failed', 'error': 'timeout'}

elec_data=main_parser()
print(elec_data)
print(int(elec_data["batteryC"]*1000))
Bcurrent=int(elec_data["batteryC"]*1000)
Bvoltage=int(elec_data["batteryV"]*1000)
BSOC=100
Pvoltage=int(elec_data["pvV"]*1000)
Senergy=0
Time=1010010101010 #elec_data["time"]
receipt=broadcastData(Bcurrent,Bvoltage,BSOC,Pvoltage,Senergy,Time)
print(receipt)
  
  







  
  

