##
##
class NetworkNode():
    def __init__(self, name, ip, location):
        self.name = name
        self.ip = ip
        self.location = location

node001 = NetworkNode('rtr001', '192.168.1.1', '1st floor')
node002 = NetworkNode('rtr002', '192.168.1.2', '2nd floor')
node003 = NetworkNode('rtr003', '192.168.1.3', '3rd floor')

print(node001.name, node002.ip, node003.location)
print(node002.name, node003.ip, node001.location)
print(node003.name, node001.ip, node002.location)

##
## End of file...
