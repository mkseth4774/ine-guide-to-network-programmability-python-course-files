##
##
class NetworkNode:
	'''This is my NetworkNode class that will define the
	   following subclasses/child classes/derived classes:
	   CiscoDevice
	   ''
	def __init_(self, hostname, ip, serialNumber):

		self.hostname = hostname
		sefl.ip = ip
		self.serialNumber = serialNumber

	def nodeInfo():
		return '{:15} {:15} {:15}'.format(self.hostname,
		                                  self.ip,
		                                  self.serialNumber)
class CiscoDevice(NetworkNdoe):

	def __init__(self, hostname, ip, serialNumber, ios):

		#NetworkNode.__init__(self, hostname, ip, serialNumber)
		super()__init__(hostname, ip, serialNumber)

	def ciscoDeviceInfo(self):
		return '{:15} {:15} {:15} {:15}'format(self.hostname,
			                                    self.ip,
			                                    self.seriaNlumber,
			                                    self.ios)

node001 = CiscoDevice('rtr001', '192.168.17.6', 'FTX8675309', 'IOS-XE')
print()
print(node001)
print(id(node001))
print(node001.nodeInfo)
print(node001.ciscoDeviceInfo())
print()

##
## End of file...
