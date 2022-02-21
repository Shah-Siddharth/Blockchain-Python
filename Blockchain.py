import hashlib
import json
import time

class Blockchain():
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(prev_hash="00000")

    def new_block(self, prev_hash):
        block_data = {
            "index": len(self.chain) + 1,
            "time_stamp": time.time(),
            "transactions": self.current_transactions,
            "previous_hash": prev_hash
        }

        data_string = json.dumps(block_data, sort_keys=True)
        nonce = 1
        (hash, nonce) = self.mine_block(data_string)

        block = {
            "index": len(self.chain) + 1,
            "time_stamp": time.time(),
            "transactions": self.current_transactions,
            "hash": hash,
            "nonce": nonce,
            "previous_hash": prev_hash
        }

        self.current_transactions.clear()
        self.chain.append(block)
        print("New block added. Hash = ", block["hash"])
        return block

    def new_transaction(self, sender, receiver, amount):
        self.current_transactions.append({"sender":sender, "receiver":receiver, "amount":amount})

    def last_block(self):
        return self.chain[-1]

    def mine_block(self, data_string):
        nonce = 1
        difficulty = 3
        while True:
            hash = hashlib.sha256((data_string + str(nonce)).encode()).hexdigest()
            if hash[:difficulty] == '0'*difficulty:
                break

            nonce += 1

        return (hash, nonce)


if __name__ == "__main__":
    testchain = Blockchain()
    testchain.new_transaction("Alice","Bob",100)
    testchain.new_transaction("Bob","Mark",50)
    testchain.new_block(testchain.last_block()["hash"])
