import hashlib
from datetime import datetime
import random

class Block:
    def __init__(self,id,data,prev_hash):
        self.blockId = id
        self.timestamp = datetime.now()
        self.data = str(data)
        self.prev_hash = prev_hash
        self.nonce = random.randint(10000,99999)
        self.hash = self.getHash()

        print("Block id : {}".format(self.blockId))
        print("Block timestamp : {}".format(self.timestamp))
        print("Block data : {}".format(self.data))
        print("Block prev_hash : {}".format(self.prev_hash))
        print("Block nonce : {}".format(self.nonce))
        print("Block hash : {}".format(self.hash))
        print("\n")

    def getHash(self):
        hash = hashlib.sha256((str(self.blockId) + str(self.timestamp)
                + str(self.data) + str(self.prev_hash) 
                + str(self.nonce)).encode())
        
        hash = hash.hexdigest()

        return hash

id = input("Enter block id: ")
data = input("enter your data: ")
prev_hash = ("0")

Blockname = Block(id,data,prev_hash)