from web3 import Web3,HTTPProvider
from web3.auto import w3
import time
from listener import listen
#import init_contract function
from init_contract import start_contract

AppContract,DataContract,w3=start_contract()

#newQRcode
#AuthorizedContract
event_auth = DataContract.events.AuthorizedContract.createFilter(fromBlock=0)
value=listen(event_auth)
print(value[0]['args'],value[0]['event'])







  
  

