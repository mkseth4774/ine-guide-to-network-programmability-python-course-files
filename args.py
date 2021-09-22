#!/usr/bin/env python3
##
##

## Importing needed modules...
from sys import exit, argv

## Main program..
if len(argv) != 3:
   exit("""
Usage: ./args.py  [hostname]  [IPv4 address]
UsageError: Two arguments required
""")

## Create empty dictionary and then populate
inventoryDict = { }
inventoryDict[argv[1]] = [argv[2]]

sumOctets = int(argv[2].split('.')[0]) + int(argv[2].split('.')[1]) + int(argv[2].split('.')[2]) + int(argv[2].split('.')[3])

print('The sum of all four (4) octets is:', sumOctets)

print('The dictionary items are:', inventoryDict.items())

##
## End of file...
