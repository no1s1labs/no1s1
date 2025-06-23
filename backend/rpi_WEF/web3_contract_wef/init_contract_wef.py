from web3 import Web3,HTTPProvider
#from web3.auto import w3
from .no1s1WEFAddress import WEFAddress
import json
#import time

def start_contract():
  with open("/home/no1s1/Documents/web3_contract/no1s1WEF.json") as na:
    WEFAbi=json.load(na)

  

  w3=Web3(HTTPProvider('https://rinkeby.infura.io/v3/d71645cb22754ded9d58d9b6b4006424'))
  WEFContract=w3.eth.contract(address = WEFAddress, abi=WEFAbi)
  WEFContract.address = WEFAddress

  return(WEFContract,w3)

 

  







  
  

