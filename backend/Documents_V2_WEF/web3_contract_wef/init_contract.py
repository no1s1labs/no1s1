from web3 import Web3,HTTPProvider
#from web3.auto import w3
from .no1s1AppAddress import AppAddress
from .no1s1DataAddress import DataAddress
import json
#import time

def start_contract():
  with open("/home/no1s1/Documents/web3_contract/no1s1App.json") as na:
    AppAbi=json.load(na)

  with open("/home/no1s1/Documents/web3_contract/no1s1Data.json") as da:
    DataAbi=json.load(da)
  

  w3=Web3(HTTPProvider('https://rinkeby.infura.io/v3/d71645cb22754ded9d58d9b6b4006424'))
  AppContract=w3.eth.contract(address = AppAddress, abi=AppAbi)
  AppContract.address = AppAddress
  DataContract=w3.eth.contract(address = DataAddress, abi=DataAbi)
  DataContract.address = DataAddress
  #print(w3.eth.block_number)
  return(AppContract,DataContract,w3)

 

  







  
  

