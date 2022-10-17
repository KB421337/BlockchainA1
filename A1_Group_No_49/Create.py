import pickle
from Blockchain import Blockchain

def Create():
    #Initializing a new blockchain
    lms = Blockchain() #Acronym for Land Management System
    #Pickling blockchain
    with open('pickle_chain.txt', 'wb') as f:
        pickle.dump(lms, f)
    return