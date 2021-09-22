##
##
class NodeClass:

    nodeType = 'IoT'

    def __init__(self, serialNumber, os, ip, location='Inventory 5th Floor', username='admin', password='cisco'):
        self.serialNumber = serialNumber
        self.os = os
        self.ip = ip
        self.location = location
        self.username = username
        self.password = password

    def nodeInfo(self):
        return '{:15} {:10} {:17} {:30} {:10} {:15}'.format(self.serialNumber, 
                                                self.os, 
                                                self.ip, 
                                                self.location, 
                                                self.username, 
                                                self.password)

    def nodeClass(self):
        return '{}'.format(self.nodeType)

node01 = NodeClass('FTX8675309', 'IOS-XE', '10.0.0.11', username='superuser')

print()
print('{:15} {:10} {:17} {:40} {:10} {:15}'.format('Serial Number', 'IOS', 'IP', 'Location', 'User', 'Password'))
print('-' * 99)
print(node01.nodeInfo())
print()
print('This node is of type: ', node01.nodeClass())
print()

##
## End of file...
