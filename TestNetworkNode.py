class NetworkNode:

    nodeClass = 'IoT'

    def __init__(self, serialNumber, os, ip, location='5th Floor Storage Room'):
        self.serialNumber = serialNumber
        self.os = os
        self.ip = ip

    def nodeInfo(self):
        print('-' * 79)
        return '{} {} {} {}'.format(self.serialNumber, self.os, self.ip, self.location)
    
    def nodeType(self):
    	return '{}'.format(self.nodeClass)

node01 = NetworkNode('FTX8675309', 'IOS-XE', '10.0.0.11')
print(node01.nodeInfo())
print(node01.nodeType())