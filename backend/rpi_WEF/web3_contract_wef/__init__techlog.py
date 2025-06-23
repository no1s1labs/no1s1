from defaultaccount import account
from encode import key
from iot.__init__parser import main_parser
#import init_contract function
from init_contract import start_contract
import web3
from hexbytes import HexBytes
from get_receipt import find_receipt
from datetime import datetime

AppContract,DataContract,w3=start_contract()

def broadcastData(Bcurrent,Bvoltage,BSOC,Pvoltage,Senergy,Time):
  nonce = w3.eth.getTransactionCount(account)

    #Calling the newReading function of contract to log readings
  txn_dict = AppContract.functions.broadcastData(Bcurrent,Bvoltage,BSOC,Pvoltage,Senergy,Time).buildTransaction({
        'chainId': 4,
        'from':account,
        'gas': 1860000,
        #'gasLimit':6994000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })
  #txn_dict['gas']=web3.eth.estimateGas(txn_dict)
  #signing the transaction 
  signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = key)
  txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
  decoded_hash=HexBytes.hex(txn_hash)
  return decoded_hash
  

elec_data=main_parser()
print(elec_data)
print(int(elec_data["batteryC"]*1000))
Bcurrent=int(elec_data["batteryC"]*1000)
Bvoltage=int(elec_data["batteryV"]*1000)
BSOC=100
Pvoltage=int(elec_data["pvV"]*1000)
Senergy=0
now=datetime.now()
Time=int(now.strftime('%Y%m%d%H%M%S')) #elec_data["time"]
decoded_hash=broadcastData(Bcurrent,Bvoltage,BSOC,Pvoltage,Senergy,Time)
print(decoded_hash)
txn_receipt=find_receipt(decoded_hash)
print('whole receipt',txn_receipt)
status=txn_receipt['status']
if status == 1:
 print('transaction successful!')
elif statuss == 0:
 print('transaction failed!')
  







  
  

