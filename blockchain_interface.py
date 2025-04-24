from web3 import Web3
import json

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.default_account = w3.eth.accounts[0]

with open("compiled_contract.json", "r") as file:
    contract_data = json.load(file)

abi = contract_data["abi"]
address = contract_data["address"]
contract = w3.eth.contract(address=address, abi=abi)

def issue_certificate(certID, pubkey, expiry, signature):
    tx_hash = contract.functions.issueCertificate(certID, pubkey, expiry, signature).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)

def verify_certificate(certID):
    return contract.functions.verifyCertificate(certID).call()

def revoke_certificate(certID):
    tx_hash = contract.functions.revokeCertificate(certID).transact()
    w3.eth.wait_for_transaction_receipt(tx_hash)
