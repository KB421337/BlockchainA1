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
    #Constructing a new blockchain for use.
    #Following parameters are specified:
    #
    #A unique identifier is generated for each block upon creation.
    def __init__(self):
        self.blockchain = [Genesis()]
        self.node_list = []
        self.transac_pool = []
        self.uuid = uuid.uuid4().hex

        #Pickling transaction pool
        with open('pickle_pool.txt', 'wb') as f:
            pickle.dump(self.transac_pool, f)

    def ProofOfElapsedTime(self, prev_hash: str, data: list):
        winner = asyncio.run(Poet())
        print("\nWinner of this round is: " + str(winner))
        concat_data = "" 
        for d in data:
            concat_data += d
        root_hash = Merkle(data)
        merged = str(prev_hash) + concat_data + root_hash
        return [sha256(merged.encode('utf-8')).hexdigest()]


    def AddTransaction(self, t: Transaction):
        #Unpickling transaction pool
        with open ("pickle_pool.txt", "rb") as f:
            self.transac_pool = pickle.load(f)
        #
        print("\n#TransacPool in beg:", len(self.transac_pool))
        #
        merged = ""
        merged += str(t.uuid) + '|' + str(t.timestamp) + '|' + str(t.push) + '|' + str(t.pubh) + '|' + str(t.amt) + '|' \
        + str(t.pub)+ '|' + str(t.propid) + '|' + str(t.pus) + '|' + str(t.digsig)
        self.transac_pool.append(merged)
        with open("Transaction_Log.txt", "a") as f:
            f.write(merged + '\n')

        #Pickling transaction pool
            with open('pickle_pool.txt', 'wb') as f:
                pickle.dump(self.transac_pool, f)
                
        if len(self.transac_pool) >= 4:
            print("\nStarting new block creation (calling PoET Consensus Algorithm)...")
            self.AddBlock()

    def verifySignature(self, S, pus, M):
        public_key_e = int(pus.split('q')[0])
        n = int(pus.split('q')[1])
        C = (S**public_key_e) % n
        if C == M:
            return True
        else:
            return False

    #Method for adding a new block.
    def AddBlock(self):
        #Unpickling transaction pool
        with open ("pickle_pool.txt", "rb") as f:
            self.transac_pool = pickle.load(f)

        print("Mining new block at height " + str(len(self.blockchain)) + "...")
        num_verified_transactions = 0
        data = []
        for t in self.transac_pool[:]:
            M = (int)(t.split('|')[-3])
            pus = t.split('|')[-2]
            pub = t.split('|')[-4]
            S = (int)(t.split('|')[-1])
            uids = -1
            uidb = -1
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
            print(uids,uidb)    
            print(len(self.node_list))
            Nodes = self.node_list[uids]
            if M in Nodes.propids:
                if (self.verifySignature(S,pus,M) == True):
                    data.append(t)
                    Nodes.delete(M)
                    Nodeb = self.node_list[uidb]
                    Nodeb.add(M)
                    num_verified_transactions += 1
                    Nodeb.showprops()
                    Nodes.showprops()
            

            self.transac_pool.remove(t)
        print("Verified Transactions: ", num_verified_transactions)
        
        if (len(data) == 0):
            print("No valid transactions to create a block.")
        else:
            prev = self.blockchain[-1].poet
            new_hash = self.ProofOfElapsedTime(prev, data)
            print("Block added. Proof(hex): ", new_hash)
            sys.stdout.flush()
            self.blockchain.append(Block(data, new_hash, prev))   
        
        #Pickling transaction pool
        with open('pickle_pool.txt', 'wb') as f:
            pickle.dump(self.transac_pool, f) 