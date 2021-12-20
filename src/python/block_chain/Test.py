from BlockChain import BlockChain

if __name__ == '__main__':
    chain = BlockChain()
    chain.add_new_block("a")
    chain.add_new_block("b")
    chain.add_new_block("c")
    chain.add_new_block("d")
    chain.add_new_block("e")
    chain.add_new_block("f")

    #chain.print_chain()
