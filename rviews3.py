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

"""This module is used to query a choice BGP server(s) on the Internet

This module will perform the following tasks:
    
    1. Each of the three (3) funcitons will create an interactive login session for
       the route server in question.
"""

__version__ = 1.0

from os import system
import pexpect

def interactSunrise():
    child = pexpect.spawn('telnet routeserver.sunrise.ch', timeout=300)
    
    child.sendline('\n')
    child.expect(['RS_AS6730>', pexpect.TIMEOUT])
    
    child.interact()
    
def interactOptus():
    child = pexpect.spawn('telnet 203.202.125.6', timeout=300)
    
    child.sendline('\n')
    child.expect(['route-views.optus.net.au>', pexpect.TIMEOUT])
    
    child.interact()

def interactOregon():
    child = pexpect.spawn('telnet route-views.oregon-ix.net', timeout=300)
    
    child.sendline('\n')
    child.expect(['Username:', pexpect.TIMEOUT])
    
    child.sendline('rviews')
    child.expect(['route-views>'])
    
    child.interact()
    
def main():
    '''
    This is the main() function that will invoke/call the other functions
    when this module is run as a script. If not being run as a script, the
    main() function will never be called.
    '''
    system('clear')
    print()
    print('Welcome to the Python BGP Rviews Menu!!!')
    print()
    
    while True:
        print('''Please make your choice from the options below:
        
        1. Interact with the Sunrise rviews router
        2. Interact with the Optus rviews router
        3. Interact with the Oregon rviews router
        4. Exit...
        ''')
        
        answer = input('What is your choice: ')
        
        if answer == '1':
            interactSunrise()
        elif answer == '2':
            interactOptus()
        elif answer == '3':
            interactOregon()
        elif answer == '4':
            exit(999)
        else:
            print('You did not enter a valid option - please try again.')
        
        
if __name__ == '__main__':
    main()
    
##
## End of file...