#!/usr/bin/env python3
##
##
attempts = 0
serialNumber = 'FTX8675309'
nodesFile = open('nodes.txt','r')
for line in nodesFile:
    if serialNumber not in line:
        print(line.strip())

nodesFile.close()
##
##
##End of file 
