from .defaultaccount import account
from .encode import key
#import init_contract function
from .init_contract_wef import start_contract
import web3
#from .qrcode import jensQR
from hexbytes import HexBytes
from .get_receipt import find_receipt

WEFContract,w3=start_contract()


def access(userqr):
  #print(account)
  #nonce = w3.eth.getTransactionCount(account)
  nonce_access = w3.eth.getTransactionCount(account) 
  print("nonce is",nonce_access)
  #Calling checkaccess function to confirm the entry of a user
  txn_dict = WEFContract.functions.buy(userqr).buildTransaction({
        'chainId': 4,
        'from':account,
        'gas': 18600000,
        #'gasLimit':6994000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce_access,
    })
  print("transaction dictionary",txn_dict)
  signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = key)
  print("signed transactino",signed_txn)
  txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
  decoded_hash=HexBytes.hex(txn_hash)
  print("transaction hash is",decoded_hash)
  return decoded_hash
  
# testuserkey=jensQR
# txn_hash=access(testuserkey)
# print(txn_hash)
# txn_receipt=find_receipt(txn_hash)
# print('whole receipt',txn_receipt)
# status=txn_receipt['status']
# if status == 1:
#  print('transaction successful!')
# elif statuss == 0:
#  print('transaction failed!')

def transactionAccess(txn_hash):
  print("transaction access starts, finding receipt....")
  txn_receipt=find_receipt(txn_hash)
  #find_receipt(txn_hash)
  print("transaction receipt is",txn_receipt)
  status=txn_receipt['status']
  if status == 1:
    return True
    print('transaction successful!')
  elif status == 0:
    print('transaction failed!')
    return False

def exit(_dooropened,_actualDuration,_userkey):
  #nonce = w3.eth.getTransactionCount(account)
  nonce_exit = w3.eth.getTransactionCount(account) 
  print("nonce is",nonce_exit)
  #Calling checkaccess function to confirm the entry of a user
  txn_dict = WEFContract.functions.exit(_dooropened,_actualDuration,_userkey).buildTransaction({
        'chainId': 4,
        'from':account,
        'gas': 18600000,
        #'gasLimit':6994000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce_exit,
    })
  signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = key)
  txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
  decoded_hash=HexBytes.hex(txn_hash)
  return decoded_hash
