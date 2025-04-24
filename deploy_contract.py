'''from solcx import compile_source, install_solc
from web3 import Web3
import json

install_solc("0.8.0")

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.default_account = w3.eth.accounts[0]

with open("CertificateRegistry.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_source(contract_source_code, output_values=["abi", "bin"])
contract_id, contract_interface = compiled_sol.popitem()

abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress

with open("compiled_contract.json", "w") as f:
    json.dump({"abi": abi, "address": contract_address}, f)

print("Contract deployed at:", contract_address)
'''

from solcx import compile_source, install_solc, set_solc_version
from web3 import Web3
import json

install_solc("0.8.0")
set_solc_version("0.8.0")  # <-- This line is important!

ganache_url = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.default_account = w3.eth.accounts[0]

with open("CertificateRegistry.sol", "r") as file:
    contract_source_code = file.read()

compiled_sol = compile_source(contract_source_code, output_values=["abi", "bin"])
contract_id, contract_interface = compiled_sol.popitem()

abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress

with open("compiled_contract.json", "w") as f:
    json.dump({"abi": abi, "address": contract_address}, f)

print("Contract deployed at:", contract_address)
