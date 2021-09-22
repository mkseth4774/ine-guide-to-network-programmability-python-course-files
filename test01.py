#!/usr/bin/env python3
##
##

def sshnodes( param1,param2,arg4,arg3):
    print('param1 is:', param1)
    print('param2 is:', param2)
    print('param3 is:', arg3)
    print('param4 is:', arg4)


arg1 = 'nodename'
arg2 = 'ip'
##arg3 = 'username'
##arg4 = 'password'

sshnodes(arg1,arg2,arg3='username',arg4='password')
##sshnodes(arg1,arg2,arg3)

##
##End of file
