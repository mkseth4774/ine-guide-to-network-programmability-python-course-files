#!/usr/bin/env python3
##
## Prompting user for needed input...
##
nodeName = input('Please enter the node name: ')
nodeIP = input('Please enter your node IP address: ')
nodeSerNum = input('Please enter your node serial number: ')

##
## Formatting and printing output...
##
print('')
print('{:12}{:20}{:15}'.format('Node Name', 'Node IP', 'Serial #'))
print('-' * 43)
print('{0:12}{1:20}{2:15}'.format(nodeName, nodeIP, nodeSerNum))
print('')

##
## End of file...
