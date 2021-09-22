##Start of Module

def funscope(param1):
  global var1
  param1 = '44:55:66:77:88'
  var1 = 'aa:bb:cc:dd:ee:ff:gg:hh'
  print('The value of var1 is:', var1)
  print('The value of param1 is:', param1)

param1 = '11:22:33:44:55'
funscope(param1)
print('The global value of var1 is:', var1)
print('The global value of param1 is:', param1)

##End of file....
