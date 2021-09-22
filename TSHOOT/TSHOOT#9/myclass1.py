##
##
class NetworkNode()
    def __init__(name, ip, location):
	self.name = name
        self.ip = ip
	self.location = location

node001 = NetworkNode('rtr001', '192.168.1.1', '1st floor')
node002 = NetworkNode('rtr002', '192.168.1.2', '2nd floor')
node003 = NetworkNode('rtr003', '192.168.1.3', '3rd floor')

print(node001, node002, node003)
print(node002, node003, node001)

##
## End of file...
