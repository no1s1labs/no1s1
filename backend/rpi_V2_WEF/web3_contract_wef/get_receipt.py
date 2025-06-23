from .init_contract import start_contract
import web3

AppContract,DataContract,w3=start_contract()

def find_receipt(txn_hash):
  txn_receipt = None
  print("finding receipt started")
  print("hashis",txn_hash)
  #check if the transaction happened and return the txhash
  while txn_receipt is None:
    try:
      txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
    except:
      pass
  return txn_receipt
