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
                print(t)
    if (len(relevant_transac) == 0):
        print("No relevant transactions for the given propid")
    else:
        print('The transactions involving property id ',pid, 'are:\n')
        for t in relevant_transac:
            tokens = t.split('|')
            qpubh = tokens[3]
            qpush = tokens[2]
            qpus = tokens[-2]
            qpub = tokens[-4]
            qts = tokens[1]
            quuid = tokens[0]
            qamt = tokens[-5]
            print("Sold by", qpush, "(", qpus, ") to", qpubh, "(", qpub, ") for", qamt, "at", qts, "(TXID:", quuid, ")\n")
