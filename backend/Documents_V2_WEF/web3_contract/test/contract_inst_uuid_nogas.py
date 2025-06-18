import time
from web3 import Web3, HTTPProvider
import contract_abi

# contract address 0x361BeE752575102cf3E00e639af2339e2Ffc4100
contract_address     = Web3.toChecksumAddress('0x361BeE752575102cf3E00e639af2339e2Ffc4100')
wallet_private_key   = "41f836406bdc879d0cddd83aeed5048d25c01313d0d45781e5cd223fb5f6bf48"
wallet_address       = Web3.toChecksumAddress('0x0307b7C3aDBBFb97ED0A12F975341f115727e7cd')


# web3.py instance
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8584"))
contract = w3.eth.contract(address = contract_address, abi = contract_abi.abi) #.abi


def retrive_useruuid():
    global uuid

    nonce = w3.eth.getTransactionCount(wallet_address)

    #Calling the newReading function of contract to log readings
    uuid=contract.functions.whatisusersuuid()

    return uuid



