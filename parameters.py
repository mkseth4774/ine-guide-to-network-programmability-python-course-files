##
##

def sshnodes(nodename, ip, password, username):
    print('param1 is:', nodename)
    print('param2 is:', ip)
    print('param3 is:', username)
    print('param4 is:', password)


nodedict = { 'nodename':'rtr342', 'ip':'10.2.3.54', 'username':'admin', 'password':'cisco' }

sshnodes(**nodedict)

##
## End of file...
