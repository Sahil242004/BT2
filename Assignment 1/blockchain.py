import os
import re

class Resume:
    def __init__(self,filename,text):
       self.filename = filename
       self.text = text

students = []

def extract_text(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    return text

folder_path = "./resume"
filenames = os.listdir(folder_path)
print(filenames)

for filename in filenames:
    text = extract_text(f"{folder_path}/{filename}")
    student = Resume(filename,text)
    students.append(student)

for student in students:
    print(student.filename)
    print(student.text)
    email = re.search(r'\S+@\S+', student.text).group()
    print(email)


import hashlib
import json
import time


def sha256(data) :
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


class Block:
    def __init__(self, index: int, timestamp: float, data: dict, previous_hash: str, nonce: int = 0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True, separators=(",", ":"))
        return sha256(block_string)
    


class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(index=0, timestamp=time.time(), data={"msg": "genesis"}, previous_hash="0")
        self.mine_block(genesis)
        self.chain.append(genesis)

 
    def last_block(self):
        return self.chain[-1]

    def is_valid_proof(self, block):
        return block.hash.startswith("0" * self.difficulty)

    def mine_block(self, block):
        while True:
            block.hash = block.compute_hash()
            print(f"Mining block {block.index}... Nonce: {block.nonce}, Hash: {block.hash}\n")
            if self.is_valid_proof(block):
                return block
            block.nonce += 1
            

    def add_block(self, data):
        new_block = Block(
            index=self.last_block().index + 1,
            timestamp=time.time(),
            data=data,
            previous_hash=self.last_block().hash
        )
        self.mine_block(new_block)
        if new_block.previous_hash != self.last_block().hash or not self.is_valid_proof(new_block):
            raise ValueError("Invalid block—rejected.")
        self.chain.append(new_block)
        return new_block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.previous_hash != prev.hash:
                return False
            if curr.compute_hash() != curr.hash:
                return False
            if not self.is_valid_proof(curr):
                return False
        return True
    
bc = Blockchain(difficulty=3)  

for student in students:
    bc.add_block(student.text)

    for b in bc.chain:
        print(f"Index: {b.index}")
        print(f"Timestamp: {b.timestamp}")
        print(f"Data: {b.data}")
        print(f"PrevHash: {b.previous_hash}")
        print(f"Nonce: {b.nonce}")
        print(f"Hash: {b.hash}")
        print("-" * 60)

    print("Chain valid?", bc.is_chain_valid())


c=1
for student in students:
    bc.chain[c].data = student.text
    c += 1
print("Chain valid after tampering?", bc.is_chain_valid())



for i in range(1, len(bc.chain)):
    bc.chain[i].previous_hash = bc.chain[i-1].hash
    bc.chain[i].hash = bc.chain[i].compute_hash()
    
    bc.mine_block(bc.chain[i])
    # bc.chain[i].nonce = 280
    print(f"Re-mined block {i}: {bc.chain[i].hash}")

print("Chain valid after recomputing?", bc.is_chain_valid())
