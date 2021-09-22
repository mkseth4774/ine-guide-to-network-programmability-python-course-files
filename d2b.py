#!/usr/bin/env python3
##
##
ipv4Address = input('Please enter an IPv4 address: ')

firstOctet = int(ipv4Address.split('.')[0])
secondOctet = int(ipv4Address.split('.')[1])
thirdOctet = int(ipv4Address.split('.')[2])
fourthOctet = int(ipv4Address.split('.')[3])

print('Your IPv4 addresss {0} in dotted binary form will be: {1:08b}.{2:08b}.{3:08b}.{4:08b}'.format(ipv4Address,firstOctet,secondOctet,thirdOctet,fourthOctet))

##
## End of file...
