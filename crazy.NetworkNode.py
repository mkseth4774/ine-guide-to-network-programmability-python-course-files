##
##
class NetworkNode:
    '''This is the class doctring...'''
    _totalNodeCount = 0

    def __init__(obj, hostname, serial, ip, brand):
        obj.hostname = hostname
        obj.serial = serial
        obj.ip = ip
        obj.brand = brand
        NetworkNode._totalNodeCount += 1

    def displayNode(obj):
        print('Node Hostname: ', obj.hostname)
        print('Node Serial Number: ', obj.serial)
        print('Node IP Address: ', obj.ip)
        print('Node Manufacturer: ', obj.brand)

print('Instantiating our first instance/object!!!')
node0001 = NetworkNode('rtr001', 'ftx8675309', '10.0.2.3', 'Cisco')
node0002 = NetworkNode('sw001', 'ftx8675302', '10.0.9.2', 'Juniper')
node0001.displayNode()
node0002.displayNode()

print('The total number of nodes in your network is: ', NetworkNode._totalNodeCount)

##
## End of file...
