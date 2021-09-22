##
##
import getpass
import pexpect
import time

username = input('Please enter your username: ')
password = getpass.getpass('Enter your secret password: ')
ip = input('Enter IP address of the device to which you wish to connect: ')
ccr = input('Enter your CCR number: ')

dateandtime = time.strftime('%m.%d.%Y_%H:%M:%S')

child = pexpect.spawnu('ssh -l ' + username + ' -c aes128-cbc ' + ip)
child.expect(['Password:'])
child.sendline(password)
child.expect(['#'])
child.sendline('terminal length 0')
child.expect(['#'])
child.sendline('show run')
child.expect(['#'])
running_config = child.before
with open('config_' + ip + '_' + dateandtime + '_' + ccr, 'w') as f:
    f.write(running_config)

##
## End of file...
