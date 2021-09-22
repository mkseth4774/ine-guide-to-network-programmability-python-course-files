#!/root/anaconda3/bin/python3
##
##
import pexpect
import time
import getpass
import re
from os import system

def getConfig(username, password, ip):

    child = pexpect.spawnu('ssh -l ' + username + ' -c aes128-cbc ' + ip)

    child.expect(['Password:'])
    child.sendline(password)

    child.expect(['#'])
    child.sendline('terminal length 0')

    child.expect(['#'])
    child.sendline('show version')

    child.expect(['#'])
    running_configuration = child.before

    try:
        with open('/tmp/config.cfg', 'w') as f:
            f.write(running_configuration)
    except FileNotFoundError:
        print('Unable to locate file!')

    try:
        with open('/tmp/config.cfg', 'r') as f:
            for line in f:
                if 'IOS Software' in line:
                    iosVersion = line.strip().split(',')[2].split(' ')[2]
 #                   print(iosVersion)
    except BaseException:
        print('Unable to locate file!')

    try:
        with open('/tmp/config.cfg', 'r') as f:
            for line in f:
                if 'Model number' in line:
                    modelNumber = line.split(':')[1].lstrip().strip()
 #                   print(modelNumber)
    except:
        print('Unable to locate file!')

    print(iosVersion, modelNumber)
    return iosVersion, modelNumber
    child.close()

def main():

    system('clear')

    username = input('Enter your username: ')
    password = getpass.getpass('Enter your password: ')
    ip = input('Enter the IP address of the device from which you want the config: ')

    getConfig(username, password, ip)

    print()
    print()
    print('{:17} {:20} {:15} {:10} {:10}'.format('IP', 'Model', 'iosVersion', 'Username', 'Password'))
    print('-' * 80)
    print('{:17} {:20} {:15} {:10} {:10}'.format(ip, modelNumber, iosVersion, username, password))
    print()
    print()

if __name__ == '__main__':
    main()

##
## End of file...
