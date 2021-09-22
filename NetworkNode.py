##
##
class NetworkNode:
	'''This is my NetworkNode class that will define the
	   following subclasses/child classes/derived classes:
	   CiscoDevice
	   JuniperDevice
	   PaloAltoDevice
	   '''
	def __init__(self, hostname, ip, serialNumber):

		self.hostname = hostname
		self.ip = ip
		self.serialNumber = serialNumber

	def nodeInfo(self):
		return '{:15} {:15} {:15}'.format(self.hostname,
		                                  self.ip,
		                                  self.serialNumber)
class CiscoDevice(NetworkNode):

	def __init__(self, hostname, ip, serialNumber, ios):

		#NetworkNode.__init__(self, hostname, ip, serialNumber)
		super().__init__(hostname, ip, serialNumber)
		self.ios = ios

	def ciscoDeviceInfo(self):
		return '{:15} {:15} {:15} {:15}'.format(self.hostname,
			                                    self.ip,
			                                    self.serialNumber,
			                                    self.ios)

class JuniperDevice(NetworkNode):

	def __init__(self, hostname, ip, serialNumber, junos):

		#NetworkNode.__init__(self, hostname, ip, serialNumber)
		super().__init__(hostname, ip, serialNumber)
		self.junos = junos

	def juniperDeviceInfo(self):
		return '{:15} {:15} {:15} {:15}'.format(self.hostname,
			                                    self.ip,
			                                    self.serialNumber,
			                                    self.junos)
class PaloAltoDevice(NetworkNode):

	def __init__(self, hostname, ip, serialNumber, panos):

		#NetworkNode.__init__(self, hostname, ip, serialNumber)
		super().__init__(hostname, ip, serialNumber)
		self.panos = panos

	def paloaltoDeviceInfo(self):
		return '{:15} {:15} {:15} {:15}'.format(self.hostname,
			                                    self.ip,
			                                    self.serialNumber,
			                                    self.panos)
class AristaDevice(NetworkNode):

	def __init__(self, hostname, ip, serialNumber, eos):

		#NetworkNode.__init__(self, hostname, ip, serialNumber)
		super().__init__(hostname, ip, serialNumber)
		self.__eos = eos

	def __aristaDeviceInfo(self):
		return '{:15} {:15} {:15} {:15}'.format(self.hostname,
			                                    self.ip,
			                                    self.serialNumber,
			                                    self.__eos)

node001 = CiscoDevice('rtr001', '192.168.17.6', 'FTX8675309', 'IOS-XE')
node002 = JuniperDevice('swi002', '10.0.0.2', 'FTX8463322', 'JUNOS 12.4')
node003 = PaloAltoDevice('5060-002', '172.16.43.22', 'PA85733339', 'PANOS 7.1')
node004 = AristaDevice('7050T-004', '10.0.99.234', 'AR6342733', 'EOS 4.11.0')
print(node001)
print(node002)
print(node003)
print(node004)
print()
print(id(node001))
print(id(node002))
print(id(node003))
print(id(node004))
print()
print(node001.nodeInfo())
print(node002.nodeInfo())
print(node003.nodeInfo())
print(node004.nodeInfo())
print()
print(node001.ciscoDeviceInfo())
print(node002.juniperDeviceInfo())
print(node003.paloaltoDeviceInfo())
print(node004._AristaDevice__aristaDeviceInfo())