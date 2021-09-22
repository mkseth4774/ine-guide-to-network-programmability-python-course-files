#!/usr/bin/env python3
##
##

def sshnodes(ip, username, password, nodename):
    print('param1 is:', nodename)
    print('param2 is:', ip)
    print('param3 is:', username)
    print('param4 is:', password)


nodedict = {'nodename':'rtr002','ip':'10.0.0.200','username':'admin','password':'cisco'}
sshnodes(**nodedict)

##
##End of file

