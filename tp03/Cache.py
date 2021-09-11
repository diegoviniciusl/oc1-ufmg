from Block import Block
from numberParser import binaryToDecimal

BLOCKS = 64
BLOCK_STRINGS = 4
BLOCK_BITS = 32
OFFSET_BITS = 2
INDEX_SIZE = 6
OFFSET_SIZE = 4
TAG_SIZE = BLOCK_BITS - INDEX_SIZE - OFFSET_SIZE

class Cache:
    def __init__(self):
        self.blocks = [Block() for i in range(BLOCKS)]
        self.hits = 0
        self.misses = 0
    
    # Rever essa caralha
    def getTag(self, address): 
        return address[: TAG_SIZE]
    
    # Rever essa caralha
    def getIndex(self, address):
        return address[TAG_SIZE : TAG_SIZE + INDEX_SIZE]
    
    # Rever essa caralha
    def getOffset(self, address):
        return address[TAG_SIZE + INDEX_SIZE : TAG_SIZE + INDEX_SIZE + OFFSET_SIZE]
    
    def hitRead(self, address):
        index = binaryToDecimal(self.getIndex(address))
        tag = self.getTag(address)

        if self.blocks[index].valid and self.blocks[index].tag == tag:
            self.hits += 1
            return True 
        return False

    def addString(self, index, stringIndex, memoryData):
        self.blocks[index].strings[stringIndex] = memoryData
    
    def setBlockTag(self, index, tag):
        self.blocks[index].tag = tag

    def setBlockValid(self, index, valid):
        self.blocks[index].valid = valid

    def setBlockDirty(self, index, dirty):
        self.blocks[index].dirty = dirty

    def isBlockDirty(self, index):
        return self.blocks[index].dirty

    def write(self, index, tag, offset, data):
        self.blocks[index].write(tag, offset, data)