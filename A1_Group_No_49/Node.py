class Node:
    # Each node is given a weight and a cash value when it is created.
    # This weight comes into play when a transaction needs to be voted upon.
    # Currently, all nodes except Dexter have a weight of 0. [they cannot vote upon any transactions]
    def __init__(self, uid: int, pu: str, pr: int, propids: list):
        self.uid = uid
        self.pu = pu
        self.pr = pr
        self.propids = propids

    def add(self,prop: int):
        self.propids.append(prop)
    
    def delete(self,prop: int):
        self.propids.remove(prop)
    
    def showprops(self):
        print("User,", self.uid," owns properties having PropIDs -",self.propids)
