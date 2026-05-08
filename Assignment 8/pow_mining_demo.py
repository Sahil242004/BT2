import hashlib
import time


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        payload = (
            f"{self.index}|{self.timestamp}|{self.data}|"
            f"{self.previous_hash}|{self.nonce}"
        )
        return hashlib.sha256(payload.encode()).hexdigest()


class SimplePoWChain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self._create_genesis()]

    def _create_genesis(self):
        genesis = Block(0, "Genesis Block", "0")
        self.mine(genesis)
        return genesis

    def mine(self, block):
        target = "0" * self.difficulty
        while not block.hash.startswith(target):
            block.nonce += 1
            block.hash = block.compute_hash()
        return block

    def add_block(self, data):
        previous = self.chain[-1]
        new_block = Block(previous.index + 1, data, previous.hash)
        mined = self.mine(new_block)
        self.chain.append(mined)

    def is_valid(self):
        target = "0" * self.difficulty
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.hash:
                return False
            if current.compute_hash() != current.hash:
                return False
            if not current.hash.startswith(target):
                return False
        return True


def main():
    print("Assignment 8: Simple Proof-of-Work Mining")
    blockchain = SimplePoWChain(difficulty=4)

    for text in ["Alice pays Bob 10", "Bob pays Charlie 4", "Charlie pays Dave 2"]:
        start = time.time()
        blockchain.add_block(text)
        elapsed = time.time() - start
        block = blockchain.chain[-1]
        print(f"\nMined Block #{block.index}")
        print(f"Data: {block.data}")
        print(f"Nonce: {block.nonce}")
        print(f"Hash: {block.hash}")
        print(f"Time: {elapsed:.3f}s")

    print("\nChain valid:", blockchain.is_valid())


if __name__ == "__main__":
    main()
