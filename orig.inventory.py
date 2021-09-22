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

"""This module will track your Cisco inventory in a flat file - written in Python 3

This module will allow you to do the following:
    
    1. Prompt the user to enter the node information
    2. Add a new node to the inventory
    3. Display a well-organized list of items in inventory
    
"""

__version__ = 1.0

from os import system

def addNode(newNode):
    '''
    This function will add a new node to the inventory file
    '''
    with open('nodes.txt', 'a') as f:
        f.write(newNode)

def printInventory():
    '''
    This function will print the current inventory file to stdout
    '''
    print('{:15}{:20}{:20}{:10}{:15}'.format('Name', 'MGMT IP', 'Serial Number', 'Username', 'Password'))
    print('-' * 75)
    with open('nodes.txt') as f:
        for line in f:
            newNode = line.strip().split(',')[0]
            nodeIP = line.strip().split(',')[1]
            nodeSerial = line.strip().split(',')[2]
            nodeUsername = line.strip().split(',')[3]
            nodePassword = line.strip().split(',')[4]
            print('{:15}{:20}{:20}{:10}{:15}'.format(newNode,nodeIP,nodeSerial,nodeUsername,nodePassword))

def main():
    '''
    This is the main() function that will invoke/call the other functions
    when this module is run as a script. If not being run as a script, the
    main() function will never be called.
    '''
    system('clear')
    
    nodeName = input('Please enter your node name: ')
    nodeIP = input('Please enter your node IP: ')
    nodeSerial = input('Please enter your node serial number: ')
    nodeUsername = input('Please enter your node username: ')
    nodePassword = input('Please enter your node password: ')
    newNode = '{},{},{},{},{}\n'.format(nodeName,nodeIP,nodeSerial,nodeUsername,nodePassword)
    addNode(newNode)
    print()
    printInventory()

if __name__ == '__main__':
    main()

##
## End of file...
