#!/usr/bin/env python3
##
##
import platform
from os import system

system('clear')
print('Welcome and here is your operating system information:')
print('')
print('Your macOS software version is:', platform.mac_ver()[0])
print('Your macOS version codename is:', platform.platform().split('-')[0])
print('Your macOS hostname is:', platform.node().split('.')[0])
print('Your macOS operating system supports:', platform.architecture()[0], 'operations')
print('')

print('Here is your Python version specific information:')
print('')
print('You are running Ptyhon:', platform.python_branch())
print('Your Python major release number is:', platform.python_version_tuple()[0])
print('Your Python minor release number is:', platform.python_version_tuple()[1])
print('Your Python patch release number is:', platform.python_version_tuple()[2])
print('This version of Python was compiled on:', platform.python_build()[1])
print('This version of Python was compiled using:', platform.python_compiler().split('(')[0])
print('')

##
## End of file...
