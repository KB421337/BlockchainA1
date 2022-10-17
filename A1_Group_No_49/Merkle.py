from hashlib import sha256
from random import randint

# Implementation of Merkle root to calculate the hash of all the transactions in a block
def Merkle(transactions: list):

    x = transactions[:]

    # SHA256 hash function
    def hash(transac):
        return sha256(transac.encode('utf-8')).hexdigest()

    # Duplicating the last transaction in case of odd number of transactions
    if len(x)%2 == 1:
            x.append(x[-1])

    # Hashing the transactions to form the leaves
    leaves = []
    for t in x:
        leaves.append(hash(t)) 

    # Recursively hashing to generate the merkle root
    def MerkleRoot(state):
        l = len(state)        
        #Reject empty states.
        if (l == 0):
            return "stateError: Empty leaf state."        
        # All leaves converged to one parent which is the merkle root.
        if (l == 1):
            print("\nMerkle root computed\n")
            return state[0]            
        #If number of nodes is odd, the last node is duplicated.
        if (l%2 == 1):
            state.append(state[-1])
        node_state = []
        for i in range(0, l, 2):
            node_state.append(hash(state[i] + state[i + 1]))        
        return MerkleRoot(node_state)

    return MerkleRoot(leaves)