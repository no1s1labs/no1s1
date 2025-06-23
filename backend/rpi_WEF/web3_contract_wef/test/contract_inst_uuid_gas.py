import time
from web3 import Web3, HTTPProvider
import contract_abi

# contract address 0x361BeE752575102cf3E00e639af2339e2Ffc4100
contract_address     = Web3.toChecksumAddress('0xfeCC962Fdc26B88B0c598Ee6Bf9EC668D6531ba9')
wallet_private_key   = "0xc9357e017039fa0f74b1278f1e68a4eb1d3fe7d6940cbad9e78051975f46cdad"
wallet_address       = Web3.toChecksumAddress('0x426289baACC0Eb101a875c66C8E8A090dD275e31')


# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi) #.abi
global d_val

def retrive_useruuid():

    nonce = w3.eth.getTransactionCount(wallet_address)

    #Calling the newReading function of contract to log readings
    txn_dict = contract.functions.whatisuseruuid().buildTransaction({
        'chainId': 8080,
        'gas': 140000,
        'gasPrice': w3.toWei('40', 'gwei'),
        'nonce': nonce,
    })

    #signing the transaction 
    signed_txn = w3.eth.account.signTransaction(txn_dict, private_key = wallet_private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = None

    #check if the transaction happened and return the txhash
    while txn_receipt is None:
        txn_receipt = w3.eth.getTransactionReceipt(txn_hash)
        #print(txn_receipt)
        #time.sleep(10)
        value=txn_receipt.logs[0]['data']
        d_val=int(value,16)
        #print(d_val)
        return d_val

    if txn_receipt is None:
        return {'status': 'failed', 'error': 'timeout'}

    
    #return {'status': 'added', 'txn_receipt': txn_receipt}
    


#def allowtime():

#    return(contract.functions.returnAllowTime().call())

