#!/usr/bin/env python3
##
##
ipv6Address = input('Please enter an IPv6 address: ')

firstHextet = int(ipv6Address.split(':')[0], 16)
secondHextet = int(ipv6Address.split(':')[1], 16)
thirdHextet = int(ipv6Address.split(':')[2], 16)

print('')
print('Your Global Routing Prefix values in decimal would be: ')
print('')
print('{:^25}{:^25}{:^25}'.format('Fisrt Hextet', 'Second Hextet', 'Third Hextet'))
print('-' * 75)

print('{0:^25}{1:^25}{2:^25}'.format(firstHextet, secondHextet, thirdHextet))
print('{0:^{align}{fill}b}{1:^{align}{fill}b}{2:^{align}{fill}b}'.format(firstHextet, secondHextet, thirdHextet, align=25, fill=0))
print('{0:^25}{1:^25}{2:^25}'.format(thirdHextet, secondHextet, firstHextet))

##
## End of file...
