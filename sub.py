#!/bin/python
##

subnetMask = input('Enter your subnet mask in dotted-decimal notation: ')

o1 = int(subnetMask.split('.')[0])
o2 = int(subnetMask.split('.')[1])
o3 = int(subnetMask.split('.')[2])
o4 = int(subnetMask.split('.')[3])

print('Your subnet mask in binary is: {0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(o1, o2, o3, o4))
print('Your subnet mask in hexadecimal is: {0:X}.{1:X}.{2:X}.{3:X}'.format(o1, o2, o3, o4))

##
## End of file...
