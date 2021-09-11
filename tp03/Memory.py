import math, sys
from numberParser import binaryToDecimal

MEMORY_WORDS = 1024

class Memory:
    def __init__(self):
        self.blocks = ['empty'] * MEMORY_WORDS

    def read(self, address):
        return self.blocks[binaryToDecimal(address)]

    def write(self, address, data):
        self.blocks[binaryToDecimal(address)] = data



