import sys
from MemoryHandler import MemoryHandler

fileName = sys.argv[1]
memoryHandler = MemoryHandler()

outFile = open("result.txt", "w")
inFile = open(fileName, "r")

rows = inFile.readlines()

results = []

for row in rows:
    inputs = row.split()
    inputs[len(inputs)-1] = inputs[len(inputs)-1].replace("\n","")
    address = str('{:032b}'.format(int(inputs[0])))
    process = inputs[1]

    if process == '0':
        response = memoryHandler.read(address)
        results.append(row.replace('\n', '') + " " + response)
    elif process == '1':
        data = inputs[2]
        memoryHandler.write(address, data)
        results.append(row.replace('\n', '') + " W")

outFile.write("READS: " + str(memoryHandler.reads) + '\n')
outFile.write("WRITES: " + str(memoryHandler.writes) + '\n')
outFile.write("HITS: " + str(memoryHandler.hits) + '\n')
outFile.write("MISSES: " + str(memoryHandler.misses) + '\n')
outFile.write("HIT RATE: " + str(round(float(memoryHandler.hits)/float(memoryHandler.reads), 3)) + '\n')
outFile.write("MISS RATE: " + str(round(float(memoryHandler.misses)/float(memoryHandler.reads), 3)) + '\n')
outFile.write('\n')

for result in results:
    outFile.write(result + '\n')

