import pickle
from Blockchain import Blockchain

def Create():
    # Initializing a new blockchain
    blockchain = Blockchain()
    
    # Pickling blockchain
    with open('pickle_chain.txt', 'wb') as f:
        pickle.dump(blockchain, f)
    return