class TestNode():
	def __init__(self, hostname, ip, os):
		self.hostname = hostname
		self.ip = ip
		self.os = os

	def nodeData(self):
		return '{} {} {}'.format(self.hostname, self.ip, self.os)
