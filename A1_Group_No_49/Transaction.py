import time
import uuid
from hashlib import sha256

class Transaction:
    # Constructor for a transaction which generates a transaction UUID to track it
    def __init__(self, uids: int, uidb: int, prs: int, propid: int, amt: int):
        self.uuid = uuid.uuid4().hex
        self.timestamp = int(time.time())

        with open('user_data.txt', 'r') as f:
            x = f.readlines()
            self.uids = uids
            self.uidb = uidb
            self.pus = x[uids-1].split(' ')[1]
            self.pub = x[uidb-1].split(' ')[1]
            self.push = sha256(self.pus.encode('utf-8')).hexdigest()
            self.pubh = sha256(self.pub.encode('utf-8')).hexdigest()

        self.amt = amt
        self.propid = propid

        variables = {'p':2081,'q':1013} 
        n = variables['p']*variables['q']
        self.digsig = int((propid**prs) % n)