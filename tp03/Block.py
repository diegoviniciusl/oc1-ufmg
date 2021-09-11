BLOCK_STRINGS = 4

class Block:
    def __init__(self):
        self.tag = 'empty'
        self.valid = False
        self.dirty = False
        self.strings = ['empty'] * BLOCK_STRINGS
    def write(self, tag, offset, data):
        self.strings[offset] = data
        self.tag = tag
        self.dirty = True
        self.valid = True
       


