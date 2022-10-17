import math
import pickle
import random
from Blockchain import Blockchain
from Node import Node
 
def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m))%m == 1):
            return x
    return -1

variables = {'p':2081, 'q':1013}
variables['n'] = variables['p']*variables['q']
variables['Pn'] = (variables['p'] - 1)*(variables['q'] - 1)

def initKeys():
    n = variables['n']
    Pn = variables['Pn']
    p_public_keys = []
    # All possible e's are such that they are not a factor of Pn
    for i in range(2, Pn):
        r =  math.gcd(Pn, i)
        if r == 1:
                p_public_keys.append(i)
    return p_public_keys 
 
p_public_keys = initKeys()
 
def createPublicKey(e_public_keys,p_public_keys):
    n = variables['n']
    while(True):
        index_max = len(p_public_keys) - 1
        rand_index = random.randint(0, index_max)
        public_key_e = p_public_keys[rand_index]
        if public_key_e not in e_public_keys:
            public_key = str(public_key_e) + 'q' + str(n)
            break
    return public_key_e, public_key
 
def createKeys(p_public_keys):
    f = open('e_keys.txt', 'r')
    e_public_keys = f.read()
    e_public_keys = e_public_keys.split('\n')[1:-1]
    e_public_keys = [int(i) for i in e_public_keys]
    f.close()
    Pn = variables['Pn']
    while(True):
        public_key_e, public_key = createPublicKey(e_public_keys, p_public_keys)
        d = modInverse(public_key_e, Pn)
        with open('e_keys.txt', 'a') as f:
            f.write(str(public_key_e) + '\n')
        if (d != -1):
            private_key = d
            break
        else:
            pass
    return public_key, private_key

def Register(): 
    create_account = input("Type Y to Create an Account and enter propertyID(s) (space separated): ")

    create_account_a = create_account.split(' ')[0]
    create_account_b = create_account.split(' ')[1:]
    pid_list = [int(pid) for pid in create_account_b]

    # Get e_public_keys from database and pass it as a parameter.
    if create_account_a == "Y" :
        public_key, private_key = createKeys(p_public_keys)
        uid = 0
        with open('num_users.txt','r') as f:
            uid = int(f.readline())
        uid = uid + 1
        with open('num_users.txt', 'w') as f:
            f.write(str(uid))
        print("Your User ID:", uid)
        print("Your Public Key :", public_key)
        print("Your Private Key :", private_key)
        print("Your property IDs: ", pid_list)
        print("\n")
    
    # Unpickling blockchain
    with open ("pickle_chain.txt", "rb") as f:
        lms = pickle.load(f) # Acronym for Land Management System

    # Creating a new node for user
    lms.node_list.append(Node(uid, public_key, private_key, pid_list))

    #Pickling blockchain
    with open('pickle_chain.txt', 'wb') as f:
        pickle.dump(lms, f)

    # Updating user data
    with open('user_data.txt', 'a') as f:
                user_data = str(uid) + ' ' + str(public_key) + ' ' + str(private_key) + ' '
                for pid in pid_list:
                    user_data = user_data + str(pid) + ' '
                user_data = user_data + '\n'
                f.write(user_data)
    
