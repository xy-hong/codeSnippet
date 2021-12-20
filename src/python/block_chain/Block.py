from hashlib import sha256
from datetime import datetime

class Block():
    
    def __init__(self, data, previous_block_hash) -> None:
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.nonce = 0
        self.hash = self.calculate_valid_hash()
        print(self.block_info())

    # 验证 hash 是否是有效的区块链 hash 值
    def is_hash_valid(self, hash: str) -> bool:
        return hash.startswith('0' * 5)

    # 计算 hash 值
    def calculate_valid_hash(self):
        hash = ""
        #nonce = 0

        while not self.is_hash_valid(hash):
            temp = self.__to_string() + str(self.nonce)
            hash = sha256(temp.encode()).hexdigest()
            self.nonce += 1
        
        return hash

    def __to_string(self) -> str:
        return f"{self.data}\t{self.timestamp}\t{self.previous_block_hash}"

    def block_info(self) -> str:
        return f"{self.data}\t{self.nonce}\t{self.timestamp}\t{self.previous_block_hash}"