#!/usr/bin/env python3

"""
This print a RIB...

More information...

"""

print("\nGateway of last resort is " + "209.165.200.226" + " to network " + "0.0.0.0\n")
print(' ' * 6 + "209.165.200.0" + "/24 " + "is variably subnetted, 2 subnets, 2 masks")
print('C' + ' ' * 8 + "209.165.200.224" + "/30 " + "is directly connected, Serial0/0/0")
print('L' + ' ' * 8 + "209.165.200.225" + "/32 " + "is directly connected, Serial0/0/0")
print('S*' + ' ' * 4 + '0.0.0.0' + '/0 [1/0] via' + ' 209.165.200.226\n')

##
## End of file...
