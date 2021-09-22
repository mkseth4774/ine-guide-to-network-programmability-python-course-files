#!/usr/bin/env python3
##
##
ipv6Address = input('Please enter an IPv6 address that is as least 48 bits long: ')

firstHextet = int(ipv6Address.split(':')[0], 16)
secondHextet = int(ipv6Address.split(':')[1], 16)
thirdHextet = int(ipv6Address.split(':')[2], 16)

print('')
print('Your hexadecimal values when converted to decimal will be: ')
print('')
print('{0:^25}{1:^25}{2:^25}'.format('First Hextet Value', 'Second Hextet Value', 'Third Hextet Value'))
print('-'*75)

print('{0:^25}{1:^25}{2:^25}'.format(firstHextet, secondHextet, thirdHextet))
print('{0:^25}{1:^25}{2:^25}'.format(thirdHextet, secondHextet, firstHextet))


##
## End of file...
