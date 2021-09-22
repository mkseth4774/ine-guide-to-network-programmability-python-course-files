#!/usr/bin/env python3
## MIT License

## Copyright (c) 2016 Travis P. Bonfigli

## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the "Software"), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in all
## copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.

"""This module is a subnet calculator and more written in Python 3

This module will tell you the following details about the subnet you enter:
    
    1. The first usable IP address in the range
    2. The last usable IP address in the range
    3. The broadcast address for your subnet
    4. The netmask in dotted-decimal notation for your subnet
    5. The total number of usable IP address in the subnet
    6. The wildcard mask of the subnet
"""

__version__ = 1.0

import ipaddress
from os import system

def hostips(network):
    '''
    This function will print out the total number of usable IPs
    '''
    numhostips = [ ]
    v4Net = ipaddress.ip_network(network)
    numhosts = v4Net.hosts()
    
    for x in numhosts:
        numhostips.append(str(x))
    
    return numhostips
    
def firsthostip(network):
    '''
    This function will print out the first usable IP for this subnet range
    '''
    numhostips = [ ]
    v4Net = ipaddress.ip_network(network)
    numhosts = v4Net.hosts()
    
    for x in numhosts:
        numhostips.append(str(x))
    
    return numhostips
    
def lasthostip(network):
    '''
    This function will print out the last usable IP for this subnet range
    '''
    numhostips = [ ]
    v4Net = ipaddress.ip_network(network)
    numhosts = v4Net.hosts()
    
    for x in numhosts:
        numhostips.append(str(x))
    
    return numhostips
    
def broadcast_address(network):
    '''
    This function will print out the broadcast address for the subnet
    '''
    broadcastAddress = ipaddress.ip_network(network)
    print('The broadcast address for this subnet would be:', broadcastAddress.broadcast_address.compressed)
    
def netmask(network):
    '''
    This function will print out the netmask in dotted-decimal notation
    '''
    dottedDecimalNetmask = ipaddress.ip_network(network)
    print('The dotted-decimal notation for the subnet mask would be:', dottedDecimalNetmask.netmask.compressed)
    
def wildcard_mask(network):
    '''
    This function will print out the wildcard mask for the subnet range
    '''
    wildcardMask = ipaddress.ip_network(network)
    print('The wildcard mask for the subnet would be:', wildcardMask.hostmask.compressed)

def main():
    '''
    This is the main() function that will invoke/call the other functions
    when this module is run as a script. If not being run as a script, the
    main() function will never be called.
    '''
    system('clear')
    network = input('Please enter a network/netmask i.e., 10.0.0.0/27: ')
    print()
    
    totalIPs = hostips(network)
    print('This subnet/mask combination will give us: ' + str(len(totalIPs)) + ' usable IPs!')
    
    firstIP = firsthostip(network)
    print('The FIRST usable IP address is:', firstIP[0])
    
    lastIP = lasthostip(network)
    print('The LAST usable IP address is:', lastIP[-1])
    
    broadcast_address(network)
    netmask(network)
    wildcard_mask(network)
    print()
    
if __name__ == '__main__':
    main()

##
## End of file...
