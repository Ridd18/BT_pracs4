import datetime
import hashlib

class Block:

    blockNo = 0
    next = None
    data = None
    hash = None
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self,data):
        self.data = data

    def hash(self):
        h = hashlib.sha256()

        h.update(
            str(self.data).encode() +
            str(self.previous_hash).encode() +
            str(self.timestamp).encode() +
            str(self.blockNo).encode() 
        )
        return h.hexdigest()
    
    def __str__(self):
        return "\n Block Hash: " + str(self.hash()) + "\nBlock No.: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nPrevious hash: " + str(self.previous_hash) +"\n--------------"

num = int(input("Enter the numberof blocks you want : "))

class Blockchain:
    print("\n For Genesis BLock")
    block = Block(input("Enter the data: "))
    head = block

    def add(self,block,data):
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1
        block.data = data
        self.block.next = block
        self.block = self.block.next

    def mine(self,block,data):
        self.add(block,data)

blockchain = Blockchain()

for n in range(num):
    print ("for block : ",n+1)
    data = input("enter the data: ")
    blockchain.mine(Block("block " + str(n+1)),data)
print('\n ..................')

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next