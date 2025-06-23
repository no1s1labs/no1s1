from web3 import Web3,HTTPProvider
from web3.auto import w3
from no1s1AppAddress import AppAddress
from no1s1DataAddress import DataAddress
import json
import time

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

try:
  while True:
    print(event_newuser.get_new_entries())
    print(event_authcontract.get_new_entries())
    time.sleep(1)
except KeyboardInterrupt:
  print('Stopped by user')




  
  

