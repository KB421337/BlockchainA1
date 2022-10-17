from hashlib import sha256
from random import randint

def Merkle(transactions: list):

    x = transactions[:]
    #SHA256 hash function. Output is a bytes object.
    def hash(transac):
        return sha256(transac.encode('utf-8')).hexdigest()

    #In case of odd number of transactions, duplicating the last transaction
    if len(x)%2 == 1:
            x.append(x[-1])
    #Hashing the transactions to form the leaves.
    leaves = []
    for t in x:
        leaves.append(hash(t)) 

    #Recursive hashing to get merkle root.
    def MerkleRoot(state):
        state_len = len(state)        
        #Reject empty states.
        if state_len == 0:
            return "stateError: Empty leaf state."        
        # All leaves converged to one parent which is the merkle root.
        if state_len == 1:
            print("\nMerkle root computed\n")
            return state[0]            
        #If number of nodes is odd, the last node is duplicated.
        if state_len%2 == 1:
            state.append(state[-1])
        node_state = []
        for i in range(0, state_len, 2):
            node_state.append(hash(state[i] + state[i + 1]))        
        return MerkleRoot(node_state)

    return MerkleRoot(leaves)