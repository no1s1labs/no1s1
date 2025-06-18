from defaultaccount import account
from encode import key
#import init_contract function
from init_contract import start_contract
import web3
from qrcode import unasQR
from hexbytes import HexBytes
from get_receipt import find_receipt

AppContract,DataContract,w3=start_contract()


def activity(distanceChanged,userqr):

  nonce = w3.eth.getTransactionCount(account)

  #Calling checkaccess function to confirm the entry of a user
  txn_dict = AppContract.functions.checkActivity(distanceChanged,userqr).buildTransaction({
        'chainId': 4,
        'from':account,
        'gas': 18600000,
        #'gasLimit':6994000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })
  signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = key)
  txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
  decoded_hash=HexBytes.hex(txn_hash)
  return decoded_hash
  
testuserkey=unasQR
sensor = True
txn_hash=access(sensor,testuserkey)
print(txn_hash)
txn_receipt=find_receipt(txn_hash)
print('whole receipt',txn_receipt)
status=txn_receipt['status']
if status == 1:
 print('transaction successful!')
elif statuss == 0:
 print('transaction failed!')
