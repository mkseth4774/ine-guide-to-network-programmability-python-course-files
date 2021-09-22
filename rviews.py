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

"""This module is used to create interactive logins with BGP route servers.

This module will perform the following tasks:
    
    1. Print a menu and ask the user to make a selection
    2. Based on that selection the module will telnet to
       one (1) of the three (3) route servers
"""

__version__ = 1.0

from os import system
import pexpect

def interactGhana():
    '''This will create an interactive login session with the Ghana route server'''
    child = pexpect.spawn('telnet route-server.mtn.com.gh', timeout = 15)
    
    child.expect(['username:', pexpect.TIMEOUT])
    child.sendline('rview')
    
    child.expect(['password:', pexpect.TIMEOUT])
    child.sendline('rview')
    
    child.expect(['mtnghana-route-server>', pexpect.TIMEOUT])
    child.sendline('\n')
    
    child.expect(['mtnghana-route-server>', pexpect.TIMEOUT])
    
    child.interact()

def interactOptus():
    '''This will create an interactive login session with the Optus route server'''
    child = pexpect.spawn('telnet 203.202.125.6', timeout = 15)
    child.sendline('\n')
    
    child.expect(['route-views.optus.net.au>', pexpect.TIMEOUT])
    
    child.interact()

def interactOregon():
    '''This will create an interactive login session with the Oregon route server'''
    child = pexpect.spawn('telnet route-views.oregon-ix.net', timeout = 15)
    child.sendline('\n')
    
    child.expect(['Username:', pexpect.TIMEOUT])
    child.sendline('rviews')
    
    child.expect(['route-views>', pexpect.TIMEOUT])
    child.sendline('\n')
    
    child.expect(['route-views>', pexpect.TIMEOUT])
    
    child.interact()

def main():
    '''This is the program main function'''
    
    system('clear')
    print()
    print('Welcome to the Python BGP Route Server Interactive Menu!!!')
    print()
    
    while True:
        print('''Please make your selection from the options below:
        
        1. Log on to the Ghana BGP route server
        2. Log on to the Optus BGP route server
        3. Log on to the Oregon BGP route server
        4. Exit...
        ''')
        
        answer = input('Which option would you like to select: ')
        
        if answer == '1':
            interactGhana()
        elif answer == '2':
            interactOptus()
        elif answer == '3':
            interactOregon()
        elif answer == '4':
            exit(99)
        else:
            print('You need to pick an option from above - please try again!')

if __name__ == '__main__':
    main()
    
##
## End of file...