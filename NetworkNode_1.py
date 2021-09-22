class NetworkNode:
    '''
    This is my networkNode Class that will define the following
    sub-classes/child classes/derived classes:
    CiscoDevice
    JuniperDevice
    Palo ALto Device
    '''

    def __init__(self, hostname, ip, serialNumber):
        self.hostname = hostname
        self.ip = ip
        self.serialNumber = serialNumber

    def nodeInfo(self):
        return '{:15} {:15} {:15}'.format(self.hostname, self.ip, self.serialNumber)


class CiscoDevice(NetworkNode):
    '''This is my Cisco Device SubClass'''
    
    def __init__(self, hostname, ip, serialNumber, ios):

        super().__init__(hostname, ip, serialNumber)
        self.ios = ios

    def ciscodeviceInfo(self):
        return '{:15} {:15} {:15} {:15}'.format(self.hostname, self.ip, self.serialNumber, self.ios)



#node001 = NetworkNode('rtr001','192.168.1.100','FTX33938524')
node001 = CiscoDevice('rtr001','192.168.1.100','FTX3985903','nx-os4.19(2.7)')
print()
print(node001.nodeInfo())
print(node001.ciscodeviceInfo())

