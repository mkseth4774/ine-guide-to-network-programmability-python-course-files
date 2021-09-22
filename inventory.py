## MIT License

## Copyright (c) 2018 Travis P. Bonfigli

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

"""This module is used to create/maintain our inventory database in a flat file

This module will perform the following tasks:
    
    1. The first function will add a node to the inventory file
    2. The second function will remove a node from the inventory file
    3. The third function will 'neatly' print out all of our inventory
    4. The fourth function will be our main() function
    5. The fifth function will check to ensure no duplicate entries are made
"""

__version__ = 1.0

from os import system

def isDuplicate(nodeSerialNumber):
    '''
    This function will check to make sure the serial number is not a duplicate
    '''   
    currentDB = open('inventory.txt').read()
    if nodeSerialNumber.upper() in currentDB:
        print('***DUPLICATE DETECTED - EXITING***')
        exit(888)
    else:
        pass

def addNode(node):
    '''
    This function will add a node to the inventory file
    '''   
    with open('inventory.txt', 'a') as f:
        f.write(node.upper())
    
    #f = open('inventory.txt', 'a')
    #f.write(node)
    #f.close()
    
def removeNode(nodeSerialNumber):
    '''
    This function will remove a node from the inventory file
    '''
    with open('inventory.txt', 'r') as f:
        tempInventoryFile = f.readlines()
    
    with open('inventory.txt', 'w') as f:
        for line in tempInventoryFile:
            if nodeSerialNumber.upper() not in line:
                f.write(line)
    
    displayInventory()
                
def displayInventory():
    '''
    This function will 'neatly' display all inventory items
    '''
    print('{:15}{:20}{:20}{:15}'.format('Node Name', 
                                        'MGMT IP', 
                                        'Serial Number', 
                                        'OS Version'))
    print('-' * 75)
    
    with open('inventory.txt', 'r') as f:
        for line in f:
            nodeName = line.strip().split(',')[0]
            nodeIP = line.strip().split(',')[1]
            nodeSerialNumber = line.strip().split(',')[2]
            nodeOS = line.strip().split(',')[3]
            print('{:15}{:20}{:20}{:15}'.format(nodeName, 
                                                nodeIP, 
                                                nodeSerialNumber, 
                                                nodeOS))
            
    #print('{}{}{}{}'.format('Node Name', 
    #                        'MGMT IP', 
    #                        'Serial Number', 
    #                        'OS Version'))
    
def main():
    '''
    This is the main() function that will invoke/call the other functions
    when this module is run as a script. If not being run as a script, the
    main() function will never be called.
    '''
    system('clear')
    print()
    
    answer = input('To ADD a node enter "1" and to DELETE a node enter "2": ')
    
    if answer == '1':
    
        print()
        nodeName = input('Please enter the node name: ')
        nodeIP = input('Please enter the node IP address: ')
        nodeSerialNumber = input('Please enter the node serial number: ')
        nodeOS = input('Please enter the node operating system version: ')
    
        #node = nodeName + ',' + nodeIP + ',' + nodeSerialNumber + ',' nodeOS
        node = '{},{},{},{}\n'.format(nodeName,nodeIP,nodeSerialNumber.upper(),nodeOS)
        isDuplicate(nodeSerialNumber.upper())
        addNode(node)
        displayInventory()
    
    elif answer == '2':
        nodeSerialNumber = input('Please enter the serial number of the node: ')
        removeNode(nodeSerialNumber.upper())
        
    else:
        print('You did not enter a "1" or a "2", please try again!')
        exit(888)
        
    print()
    
if __name__ == '__main__':
    main()

##
## End of file...