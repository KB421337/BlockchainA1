# GROUP 49 - Blockchain Assignment 1

# Land Management System

A blockchain based land management system using the PoET consensus algorithm.

## Important
The PoET algorithm is implemented in file ***Poet.py*** 
## Features

- Ability to register new users to the system with previously owned property. (implemented in file ***Register.py***)
- User can buy and sell a property. (implemented in file ***Main.py*** in the AddTransac() function)
- Incorporation of 'Proof of Elapsed Time' consensus algorithm to improve the security of the blockchain. (implemented in file ***Poet.py***)
- Implementation of Merkle root to calculate the hash of all the transactions in a block. (implemented in file ***Merkle.py***)
- Users can view the transaction history that is related to a property. (implemented in file ***Search.py***)


## Code Components
### Block 

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `timestamp` | `int` | Autogenerated time stamp |
| `prevhash` | `string` | The hash of the previous block |
| `data` | `string` |  The transaction data to be stored in the block. |
| `poet` | `string` |  The hash of [prev_block_hash + block_data + merkle_root] generated by the winner via Proof of Elapsed Time. |

### Functions
### Blockchain.py
 
| Functions | Description    |
| :-------- |:------------------------- |
| `ProofOfElapsedTime(self, prev_hash: str, data: list) `| calls `poet` to get the winner node, and returns the block hash. [prev hash + block data + merkle root]| 
|`AddTransaction(self, t: Transaction)`|adds a transaction to the transaction pool,  a new block is added if entries in pool >= 4|
|`verifySignature(self, S, pus, M)`|verifies if the transaction was done by the correct user by using cryptography|
|`AddBlock(self)`|mines a new block, if all the transactions are verified the block is added to the blockchain|


 ### Create.py
 
 | Functions | Description    |
 | :-------- |:------------------------- |
 |`Create()`| Initialises a new blockchain|


 ### Main.py
 
 | Functions | Description    |
 | :-------- |:------------------------- |
 |`AddTransac()`| Takes transaction details from user to add to blockchain|

 
 ### Merkle.py
 
 | Functions | Description    |
 | :-------- | :------------------------- |
 |`Merkle(transactions: list)`| Hash all the transactions in the list and append them to a new list|
 |`MerkleRoot(state)`| Recursive hashing to get merkle root.|


 ### Poet.py
 
 | Functions | Description    |
 | :-------- | :------------------------- |
 |`Poet()`| Asynchronous function to implement proof of elapsed time algorithm| 
 |`NodeWait(node: str, delay: float)`| Asynchronous function to make a node wait for `delay` time|

 ### Register.py
 
 | Functions | Description    |
 | :-------- | :------------------------- |
 |`createPublicKey(e_public_keys, p_public_keys)`| Creates and returns public key of user using cryptography|
 |`createKeys(p_public_keys)`| Creates and returns public and private key of user using cryptography|
 |`Register()`| Registers a new user by creating a new node for the user|
 

 ### Search.py
 
 | Functions | Description    |
 | :-------- | :------------------------- |
 |`Search(blockChain)`| Prints the transaction history of the `property id` given as input from the blockchain|

## Group Details

### GROUP 49

| Name | ID     | 
| :-------- | :------- |
| `Kaustubh Bhanj` | `2019A7PS0009H` | 
| `Dhruv Gupta` | `2019B3A70487H` |
| `Gaurav Sinha` | `2019A7PS0131H` |  
| `Bokkasam Venkata Sai Ruthvik` | `2019A7PS0017H` |  
