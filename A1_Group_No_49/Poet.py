import asyncio
from random import uniform
from time import sleep

# Incorporating a consensus algorithm (Proof of Elapsed Time) to improve the security of the blockchain:
#
# Nodes of the network are put to sleep for a given duration allotted to them through a random lottery
# The first node to wake up is the winner of the block and gets to add his block to the blockchain
# Since the nodes go to sleep concurrently, this is simulated using async functions using the inbuilt asyncio library

# The wait function
async def NodeWait(node: str, delay: float):
    await asyncio.sleep(delay)
    print(node," done waiting")

# The function which implements the Proof of Elapsed Time consensus algorithm
async def Poet():
    time_map = {}
    wait_min = 5
    winner = ""

    #Since the uids of user nodes are generated serially, total number of users gives us the list of uids
    with open('num_users.txt', 'r') as f:
        nodes = int(f.readline())

    for node in range(1, nodes + 1):
        time_map[node] = uniform(1, 4)

        # Evaluating the winner of this round
        if time_map[node] < wait_min:
            wait_min = time_map[node]
            winner = str(node)

    for node in time_map:
        print("\nUser with uid ", node, " will wait for: ", time_map[node], " seconds")

    print("\nWaiting...\n")
    wait_list = []
    
    for node in time_map:
        # Running the function passed as argument asynchronously using inbuilt asyncio library
        wait_task = asyncio.create_task(NodeWait(node, time_map[node]))
        wait_list.append(wait_task)
    
    for w in wait_list:
        # Using the await call to run all tasks concurrently
        await w

    return winner