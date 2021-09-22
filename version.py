##
##
import pexpect

def get_devices_list():

    ecc_devices = [ ]

    with open('eccnodes.txt') as f:
        for line in f:
            ecc_devices.append(line.strip())

    print('Devices:', ecc_devices)
    return ecc_devices

def telnet(ip, user, password):

    print('Connecting via telnet to: ', ip, user, password)
    telnetcmd = 'telnet' + ip

    session = pexpect.spawn('telnet' + ip, timeout=20)
    result = session.expect(['Username:', pexpect.TIMEOUT])

    if result !=0:
         print('TELNET failed connecting to:', ip)
         exit()

    session.sendline(user)
    result = session.expect(['Password:', pexpect.TIMEOUT])

    if result !=0:

##
## End of file..
