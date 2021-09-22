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

__version__ = 1.8

import ipaddress
from os import system

def allips(network):
    '''
    This function will return a list object with string elements of all usable IPs
    in the specified subnet/mask range
    '''
    allHostsList = [ ]
    v4Net = ipaddress.ip_network(network)
    allHosts = v4Net.hosts()
    
    for x in allHosts:
        allHostsList.append(str(x))
    
    return allHostsList
    
def broadcast_address(network):
    '''
    This function will print out the broadcast address for the subnet
    '''
    broadcastAddress = ipaddress.ip_network(network)
    
    return broadcastAddress
    
def netmask(network):
    '''
    This function will print out the netmask in dotted-decimal notation
    '''
    dottedDecimalNetmask = ipaddress.ip_network(network)
    
    return dottedDecimalNetmask
    
def wildcard_mask(network):
    '''
    This function will print out the wildcard mask for the subnet range
    '''
    wildcardMask = ipaddress.ip_network(network)
    
    return wildcardMask

def main():
    '''
    This is the main() function that will invoke/call the other functions
    when this module is run as a script. If not being run as a script, the
    main() function will never be called.
    '''
    system('clear')
    network = input('Please enter a network/netmask i.e., 10.0.0.0/27: ')
    print()
    
    allHosts = allips(network)
    print('This subnet/mask combination will give us: ' + str(len(allHosts)) + ' usable IPs!')
    
    allHosts = allips(network)
    print('The FIRST usable IP address is:', allHosts[0])
    
    allHosts = allips(network)
    print('The LAST usable IP address is:', allHosts[-1])
    
    bcastAddr = broadcast_address(network)
    print('Your broadcast address will be:', bcastAddr.broadcast_address.compressed)
    
    v4netmask = netmask(network)
    print('Your netmask in dotted-decimal notation would be:', v4netmask.netmask.compressed)
    
    wcardMask = wildcard_mask(network)
    print('Your wildcard mask for this subnet/mask range would be:', wcardMask.hostmask.compressed)
    
    print()
    
if __name__ == '__main__':
    main()

##
## End of file...