##
##
import pexpect

child = pexpect.spawn('telnet route-views.oregon-ix.net', timeout = 50000)
child.sendline('\n')

child.expect(['Username:'])
child.sendline('rviews')

child.expect(['route-views>'])
child.sendline('term length 0')

child.expect(['route-views>'])
child.sendline('sh ip bgp')

child.expect(['route-views>'])

with open('/tmp/bestpath.txt', 'w') as f:
    
    f.write(child.before.decode('utf-8'))

##
## End of file...
