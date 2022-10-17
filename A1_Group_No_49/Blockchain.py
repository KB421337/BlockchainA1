import asyncio
import pickle
import sys
import uuid
from hashlib import sha256
from Block import Block, Genesis
from Merkle import Merkle
from Node import Node
from Poet import Poet
from Transaction import Transaction

class Blockchain:
    # Constructing a new blockchain for use
    def __init__(self):
        self.blockchain = [Genesis()]
        self.node_list = []
        self.transac_pool = []
        self.uuid = uuid.uuid4().hex

        # Pickling transaction pool
        with open('pickle_pool.txt', 'wb') as f:
            pickle.dump(self.transac_pool, f)
    
    # Method for verifying signatures
    def verifySignature(self, S, pus, M):
        public_key_e = int(pus.split('q')[0])
        n = int(pus.split('q')[1])
        C = (S**public_key_e) % n
        if C == M:
            return True
        else:
            return False

    def ProofOfElapsedTime(self, prev_hash: str, data: list):
        # Running Poet.py to find winner
        winner = asyncio.run(Poet())
        print("\nWinner of this round is: " + str(winner))
        concat_data = "" 
        for d in data:
            concat_data += d
        root_hash = Merkle(data)
        merged = str(prev_hash) + concat_data + root_hash
        # Returning the hash of the entire block
        return [sha256(merged.encode('utf-8')).hexdigest()]

    # Method for adding a new transaction to the blockchain
    def AddTransaction(self, t: Transaction):
        # Unpickling blockchain
        with open ("pickle_chain.txt", "rb") as f:
            lms = pickle.load(f)
        # Unpickling transaction pool
        with open ("pickle_pool.txt", "rb") as f:
            lms.transac_pool = pickle.load(f)
        
        merged = ""
        merged += str(t.uuid) + '|' + str(t.timestamp) + '|' + str(t.push) + '|' + str(t.pubh) + '|' + str(t.amt) + '|' \
        + str(t.pub)+ '|' + str(t.propid) + '|' + str(t.pus) + '|' + str(t.digsig)
        lms.transac_pool.append(merged)
        with open("Transaction_Log.txt", "a") as f:
            f.write(merged + '\n')

        # Pickling updated transaction pool
            with open('pickle_pool.txt', 'wb') as f:
                pickle.dump(lms.transac_pool, f)
        # Pickling updated blockchain
        with open('pickle_chain.txt', 'wb') as f:
            pickle.dump(lms, f)
                
        # Starting process of addition of new block if number of transactions crosses four
        if len(lms.transac_pool) >= 4:
            print("\nStarting new block creation (calling PoET Consensus Algorithm)...")
            lms.AddBlock()

    # Method for adding a new block to the blockchain
    def AddBlock(self):
        # Unpickling blockchain
        with open ("pickle_chain.txt", "rb") as f:
            lms = pickle.load(f)
        # Unpickling transaction pool
        with open ("pickle_pool.txt", "rb") as f:
            lms.transac_pool = pickle.load(f)

        print("Mining new block at height " + str(len(lms.blockchain)) + "...")
        num_verified_transactions = 0
        data = []
        for t in lms.transac_pool[:]:
            M = (int)(t.split('|')[-3])
            pus = t.split('|')[-2]
            pub = t.split('|')[-4]
            S = (int)(t.split('|')[-1])
            uids = 0
            uidb = 0
            with open("user_data.txt","r") as f:
                lines = f.readlines()
                for line in lines:
                    uids += 1
                    if (line.split(' ')[1] == pus):
                        break
                for line in lines:
                    uidb += 1
                    if (line.split(' ')[1] == pub):
                        break
            node_s = lms.node_list[uids - 1]
            if M in node_s.propids:
                if (lms.verifySignature(S, pus, M) == True):
                    data.append(t)
                    node_s.delete(M)
                    node_b = lms.node_list[uidb - 1]
                    node_b.add(M)
                    num_verified_transactions += 1            

            lms.transac_pool.remove(t)
        
        if (len(data) == 0):
            print("No valid transactions to create a block.")
        else:
            prev = lms.blockchain[-1].poet
            new_hash = lms.ProofOfElapsedTime(prev, data)
            print("Block added. Proof(hex): ", new_hash)
            sys.stdout.flush()
            lms.blockchain.append(Block(data, new_hash, prev)) 
            
        # Pickling updated transaction pool
        with open('pickle_pool.txt', 'wb') as f:
            pickle.dump(lms.transac_pool, f) 
        # Pickling updated blockchain
        with open('pickle_chain.txt', 'wb') as f:
            pickle.dump(lms, f)