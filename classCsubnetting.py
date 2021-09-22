#!/usr/bin/env python3
##

from os import system
import ipaddress

system('clear')

slash24Net = ipaddress.ip_network(input('Please enter a /24 network (i.e., 192.168.1.0/24): '))
newNetmask = int(input('Please enter the new subnet mask length: '))
maskDiff = newNetmask - 24

newSubnets = [ ]

print('')
print('Subnetting your /24 with a netmask of /' + str(newNetmask) + ' will give you the following networks:')
print('-' * 80)

for subnets in (ipaddress.ip_network(str(slash24Net)).subnets(prefixlen_diff=maskDiff)):
    newSubnets.append(str(subnets))
    print(subnets)
print('')
print('From your /24, you were able to create ' + str(len(newSubnets)) + ' new subnets!!!')
print('')
print('Your Python list of the new subnets would be:', newSubnets)

print('')
print('Here is a list of the usable IPs from the 2nd subnet:')
usableIPs = [ ] 
for hosts in ipaddress.ip_network(newSubnets[1]).hosts():
    usableIPs.append(str(hosts))
    print(hosts)
print('')
print('Hey, did you know that each of your subnets has ' + str(len(usableIPs)) + ' usable IP addresses?')
print('')

##
## End file...
