import hashlib

class NeuralCoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Shuvo sends 2 NC to Dhrubo"
t2 = "Karim sends 4.1 NC to Dhrubo"
t3 = "Dhrubo sends 3.2 NC to Karim"
t4 = "Sadik sends 0.3 NC to Shuvo"
t5 = "Dhrubo sends 1 NC to Emon"
t6 = "Dhrubo sends 5.4 NC to Sadik"

initial_block = NeuralCoinBlock("Initial String", [t1, t2,])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)




