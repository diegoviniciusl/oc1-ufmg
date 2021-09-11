from Cache import Cache
from Memory import Memory
from numberParser import binaryToDecimal, decimalToBinary

CACHE_BLOCK_STRINGS = 4
STRING_BITS = 32
INDEX_SIZE = 6
OFFSET_SIZE = 4
TAG_SIZE = STRING_BITS - INDEX_SIZE - OFFSET_SIZE

class MemoryHandler:
    def __init__(self):
        self.cache = Cache()
        self.memory = Memory()
        self.hits = 0
        self.misses = 0
        self.writes = 0
        self.reads = 0

    # Rever essa caralha
    def getTag(self, address): 
        return address[: TAG_SIZE]
    
    # Rever essa caralha
    def getIndex(self, address):
        return address[TAG_SIZE : TAG_SIZE + INDEX_SIZE]
    
    # Rever essa caralha
    def getOffset(self, address):
        return address[INDEX_SIZE : INDEX_SIZE + OFFSET_SIZE]
    
    def read(self, address):
        hitCache = self.cache.hitRead(address)
        self.reads += 1

        if hitCache:
            self.hits += 1
            return "H"
        else:
            indexBinary = self.getIndex(address)
            index = binaryToDecimal(indexBinary)
            tag = self.getTag(address)
            for stringIndex in range(CACHE_BLOCK_STRINGS):
                memoryData = self.memory.read(tag + indexBinary + decimalToBinary(stringIndex))
                self.cache.addString(index, stringIndex, memoryData)
            self.cache.setBlockTag(index, tag)
            self.cache.setBlockValid(index, True)
            self.misses += 1
            return "M"

    def write(self, address, data):
        index = binaryToDecimal(self.getIndex(address))
        offset = binaryToDecimal(self.getOffset(address))
        tag = self.getTag(address)

        if self.cache.isBlockDirty(index):
            self.writeBack(address, data, index)
        
        self.cache.write(index, tag, offset, data)
        self.writes += 1

    # Rever essa porra
    def writeBack(self, address, data, index):
        self.memory.write(address, data)
        self.cache.setBlockDirty(index, False)