## MIT License

## Copyright (c) 2015 Travis P. Bonfigli

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

'''A super cool module that provides you with the critical information regarding your subnet!

   This module will give you all kinds of information about the subnet you enter.

'''

__version__ = 1.0

import ipaddress
from os import system

def broadcast(network):
    '''
    This function prints out the broadcast address for this subnet/mask pair as a string.
    '''

    bcast = ipaddress.ip_network(network)
    print('Your network broadcast address will be:', bcast.broadcast_address.compressed)

def wildcard(network):
    '''
    This function prints out the wildcard mask for this subnet/mask pair as a string.
    '''

    wildcardmask = ipaddress.ip_network(network)
    print('Your wildcard mask will be:', wildcardmask.hostmask.compressed)

def usableips(network):
    '''
    This function prints out the number of usalbe host IPs for this subnet/mask pair as an integer.
    '''

    numips = [ ]
    net = ipaddress.ip_network(network)
    numhosts = net.hosts()

    for x in numhosts:
        numips.append(str(x))

    print('You will have a total of ' + str(len(numips)) + ' usable IP addresses in your subnet.')

def netmask(network):
    '''
    This function prints out the dotted-decimal notation for the subnet mask for this subnet/mask pair.
    '''

    netmask = ipaddress.ip_network(network)
    print('The dotted-decimal subnet mask will be: ', str(netmask.netmask))

def firstusableip(network):
    '''
    This function prints out the first usable IP address for this subnet/mask pair as a string.
    '''

    ips = [ ]
    net = ipaddress.ip_network(network)
    hosts = net.hosts()
    
    for x in hosts:
        ips.append(str(x))

    print('The first usable IP address in this network will be:', ips[0])

def lastusableip(network):
    '''
    This function prints out the last usable IP address for this subnet/mask pair as a string.
    '''

    ips = [ ]
    net = ipaddress.ip_network(network)
    hosts = net.hosts()
    
    for x in hosts:
        ips.append(str(x))

    print('The last usable IP address in this network will be:', ips[-1])

def main():
    '''
    This is the main function call that will prompt the user for input and then run all functions.
    '''

    system('clear')
    network = input('Please enter your subnet and mask (i.e. 192.168.1.0/24): ')
    print('')
    firstusableip(network)
    lastusableip(network)
    broadcast(network)
    netmask(network)
    usableips(network)
    wildcard(network)
    print('')

if __name__ == '__main__':
    main()

##
## End of file...
