#!/usr/bin/env python3
##
print('Entering information for node 1 of 2: ')
node01Name = input('Please enter the node name: ')
node01IP = input('Please enter the IP: ')
node01Serial = input('Please enter the serial number: ')
node01OS = input('Please enter the operating system: ')

print('')
print('Entering information for node 2 of 2: ')
node02Name = input('Please enter the node name: ')
node02IP = input('Please enter the IP: ')
node02Serial = input('Please enter the serial number: ')
node02OS = input('Please enter the operating system: ')
print('')

node01List = [ node01Name, node01IP, node01Serial, node01OS ]
node02List = [ node02Name, node02IP, node02Serial, node02OS ]

node01Dict = {'name':node01Name, 'ip':node01IP, 'serial':node01Serial, 'os':node01OS}
node02Dict = {'name':node02Name, 'ip':node02IP, 'serial':node02Serial, 'os':node02OS}

networkNodesDict = { }
networkNodesDict[1] = node01List
networkNodesDict[2] = node02List
print(networkNodesDict)
print('')

networkNodesDict2 = { }
networkNodesDict2[1] = node01Dict
networkNodesDict2[2] = node02Dict
print(networkNodesDict2)
print('')

##
## End of file...
