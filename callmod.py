##
##
import subnet
from subnet import usableips
network = input('Please enter your network: ')
print(subnet.broadcast(network))
print(usableips(network))
