##
##
import pexpect

class RouteServer:
	'''This class will instantiate an object that
	we will use to connect via pexpect to a BGP
	route server of our choosing...
	'''
	def __init__(self, routeServer):
		'''This is my constructor'''
		self.routeServer = routeServer

	def telnetConnect(self):
		'''This is my method!'''
		self.session = pexpect.spawn('telnet ' + self.routeServer)
		#session = pexpect.spawn('telnet' + routeServer)
		#session.sendline('\n')
		self.session.sendline('\n')
		#session.expect(['>'])
		self.session.expect(['>'])
		#session.interact()
		self.session.interact()

optus = RouteServer('203.202.125.6')
optus.telnetConnect()