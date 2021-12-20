from Block import Block

class BlockChain():

    def __init__(self) -> None:
        self.blocks = []
        self.__set_genesis_block()
    
    def __set_genesis_block(self):
        genesis_block = Block("pangu", '0' * 64)
        self.blocks.append(genesis_block)

    def __get_last_block(self) -> Block:
        return self.blocks[-1]

    def add_new_block(self, data):
        last_block = self.__get_last_block()
        new_block = Block(data, last_block.hash)
        self.blocks.append(new_block)

    def print_chain(self):
        for block in self.blocks:
            print(block.block_info())
    