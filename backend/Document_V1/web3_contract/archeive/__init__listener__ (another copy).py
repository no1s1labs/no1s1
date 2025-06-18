from web3 import Web3,HTTPProvider
from web3.auto import w3
import time
#import init_contract function
from init_contract import start_contract

AppContract,DataContract,w3=start_contract()

def listen():
  event_newuser = DataContract.events.newQRcode.createFilter(fromBlock=0)
  allevent_newuser=event_newuser.get_all_entries()
  event_authcontract= DataContract.events.AuthorizedContract.createFilter(fromBlock=0)
  allevent_authcontract=event_authcontract.get_all_entries()

  event_value=event_authcontract.get_new_entries()
  while bool(event_value) is False:
    try:
      event_value=event_authcontract.get_new_entries()
    except KeyboardInterrupt:
      print("user interttupt the process")
      
  return event_value
    
value=listen()
print(value[0]['args'],value[0]['event'])
#try:
  #while True:
    #print(bool(event_newuser.get_new_entries()))
    #print(event_authcontract.get_new_entries())
    #time.sleep(1)
#except KeyboardInterrupt:
  #print('Stopped by user')




  
  

