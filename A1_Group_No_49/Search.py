from Blockchain import Blockchain

# Viewing the transaction history that is related to a property
def Search(blockChain):
    pid = input("Enter property id to get the related transaction history: ")
    len_chain = len(blockChain)
    relevant_transac = []
    for i in range(1, len_chain):
        curr_block = blockChain[i]
        transaction_list = curr_block.data
        for t in transaction_list:
            propid = t.split('|')[-3]
            if (propid == pid):
                relevant_transac.append(t)

    if (len(relevant_transac) == 0):
        print("\nNo relevant transactions for the given propid")
    else:
        print('\nThe transactions involving property id', pid, 'are:\n')
        for t in relevant_transac:
            tokens = t.split('|')
            quuid = tokens[0]
            qts = tokens[1]
            qpush = tokens[2]
            qpubh = tokens[3]
            qamt = tokens[-5]
            qpub = tokens[-4]
            qpus = tokens[-2]
            # Displaying the relevant transaction
            print("Sold by", qpush, "(", qpus, ") to", qpubh, "(", qpub, ") for", qamt, "at", qts, "(TXID:", quuid, ")\n")