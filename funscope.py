##
##

def funscope():
    global list1 
    list1 = [1,2,3,4,5]
    list1.append('Hello there')
    wwn = '0050.568c.7dcf'
    print('Inside the function the value of list is: ', list1)

list1 = list('abcdefghijklmnopqrstuvxyz')
print('Before function invocation, the list is:' , list1)
funscope()
print('Outside the function the value of list is:', list1)

##
##End of file

