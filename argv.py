#! /usr/bin/env python3
##
##
from sys import argv
#from sys import argv as args

if len(argv)  < 2:
##    exit("""
##RaiseArgumentException: Need at lease 1 command line argument
##""")
   exit(88)

#print(argv)
print(argv[1:])

##
##End of file
