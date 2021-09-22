##
##
import getpass
import pexpect

username = input('Please enter your username: ')
password = getpass.getpass('Enter your secret password: ')
ip = input('Enter IP address of the device to which you wish to connect: ')

child = pexpect.spawnu('ssh -l ' + username + ' -c aes128-cbc ' + ip)
child.expect(['Password:'])
child.sendline(password)
child.expect(['#'])
child.sendline('\n')
child.expect(['#'])

child.sendline('ssh -l ' + username + ' -c aes128-cbc 192.168.1.2')
child.expect(['Password:'])
child.sendline(password)
child.expect(['#'])
child.sendline('\n')
child.expect(['#'])

child.interact()

##
## End of file...
