transactions = [None, None, None, None, None, None]
transactions[0] = b'Sasha,12:05,Python'
transactions[1] = b'Dima,12:10,Python'
transactions[2] = b'Sasha,12:11,Python'
transactions[3] = b'Nikita,12:15,C#'
transactions[4] = b'Vitaly,12:16,Python'
transactions[5] = b'Alexey,12:20,Python'


class Block_chain:
    def __init__(self, events):
        self.block_size = 2
        self.__count = len(events)

    def count(self):
        return self.__count

    def add(self, events):
        self.__count += len(events)



block = Block_chain(transactions)
assert block is not None
assert block.block_size == 2
assert block.count() == 6
block.add([transactions[4], transactions[5]])
assert block.count() == 8
