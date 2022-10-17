class Node:
    # Each node is given has a unique, serially-generated uid, a public key, a corresponding private key 
    # and a list of propertis owned (stored in the form of their propids)
    def __init__(self, uid: int, pu: str, pr: int, propids: list):
        self.uid = uid
        self.pu = pu
        self.pr = pr
        self.propids = propids

    # Adding a new property when it is bought
    def add(self, prop: int):
        self.propids.append(prop)
    
    # Removing a property when it is sold
    def delete(self, prop: int):
        self.propids.remove(prop)
    
    # Displaying all the properties owned by the user of the node
    def showprops(self):
        print("User", self.uid,"owns properties having PropIDs -", self.propids)