# BITS F452: Blockchain Technology - Assignment 1
# - Gaurav Sinha                 | 2019A7PS0131H
# - Kaustubh Bhanj               | 2019A7PS0009H
# - Dhruv Gupta                  | 2019B3A70487H
# - Bokkasam Venkata Sai Ruthvik | 2019A7PS0017H

import pickle
from Create import Create
from Blockchain import Blockchain
from Register import Register
from Search import Search
from Transaction import Transaction

print("\nBITS F452: Blockchain Technology - Assignment 1")
print("Programmed by Group 49:                          ")
print("\t1. Gaurav Sinha                 | 2019A7PS0131H")
print("\t2. Kaustubh Bhanj               | 2019A7PS0009H")
print("\t3. Dhruv Gupta                  | 2019B3A70487H")
print("\t4. Bokkasam Venkata Sai Ruthvik | 2019A7PS0017H")

#Creating a new blockchain (executed only once)
with open('num_users.txt', 'r') as f:
    uid = int(f.readline())
    if (uid == 0):
        Create()

# Unpickling blockchain
with open ("pickle_chain.txt", "rb") as f:
    lms = pickle.load(f) # Acronym for Land Management System


# The user can buy and sell property
# The transaction is recorded by the seller (since it is vital that he agrees to the selling of his land),
# and is entered with all relevant details, including his (seller's) Private Key
def AddTransac():
    # Getting the details of the transaction from the seller
    with open('num_users.txt', 'r') as f:
        n = int(f.readline())
    print("\nType the details of the transaction: \n(please ensure that you are the seller, and that you own the land you wish to sell)")
    uids = (int)(input("Enter your uid: "))
    if ((uids > n) | (uids < 1)):
        print("Invalid uid! Transaction invalidated!!")
        pass
    else:
        uidb = (int)(input("Enter buyer's uid: "))
        if ((uidb > n) | (uidb < 1)):
            print("Invalid uid! Transaction invalidated!!")
            pass
        elif (uidb == uids):
            print("You cannot sell the land to yourself! Transaction invalidated!!")
            pass
        else:
            prs = (int)(input("Enter your private key (for generating digital signature): "))
            propid = (int)(input("Enter the land's propid (integer): "))
            amt = (int)(input("Enter the amount the land is being sold for: "))

            # Creating an object of the Transaction class
            t = Transaction(uids, uidb, prs, propid, amt)

            # Adding the transaction to the blockchain
            lms.AddTransaction(t)
            print("\nTransaction successfully added with UUID " + t.uuid) 


# Code to get inputs from user
opt = 0
while (opt != 4):    
    opt = int(input("\nChoose option:\n1.Register new user 2.Add transaction 3. Search property history 4.Exit\n"))
    
    if (opt == 1):
        Register()
        # Unpickling updated blockchain
        with open ("pickle_chain.txt", "rb") as f:
            lms = pickle.load(f)

    elif (opt == 2): 
        AddTransac()
        # Unpickling updated blockchain
        with open ("pickle_chain.txt", "rb") as f:
            lms = pickle.load(f)

    elif (opt == 3):
        Search(lms.blockchain)

    elif (opt == 4):
        # Pickling updated blockchain
        with open('pickle_chain.txt', 'wb') as f:
            pickle.dump(lms, f)
        print("\nTHANK YOU\n")

    else:
        print("Invalid option. Try Again.\n")