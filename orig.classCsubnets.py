#!/usr/bin/env python3
##
##
import ipaddress
from os import system

system('clear')

v4Slash24 = ipaddress.ip_network(input('Please enter an IPv4 /24 network (i.e., 1.2.3.0/24): ' ))
cidr = int(input('Enter your new subnet length (between 25 and 30): '))
maskDiff = cidr - 24

newCIDR = [ ]
print('')
print('Subnetting your /24 with a netmask of /' + str(cidr) + ' gives you the following networks:')
print('-' * 75)

for subnets in (ipaddress.ip_network(str(v4Slash24)).subnets(prefixlen_diff=maskDiff)):
     newCIDR.append(str(subnets))
     print(subnets)

print('')
print('From your original /24, you have now created: '+ str(len(newCIDR)) + ' subnets!!!')
print('')
print('Your list of new subnets would be:', newCIDR)
print('')
print('The usable IPs in the 1st subnet would be:')

usableIPs = [ ]
for hosts in ipaddress.ip_network(newCIDR[0]).hosts():
    usableIPs.append(str(hosts))
    print(hosts)

print('')
print('WOW! That is a total of ' + str(len(usableIPs)) + ' usable IP addresses!')
print('')

##
## End of file...
