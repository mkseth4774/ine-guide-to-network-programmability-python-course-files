#!/usr/bin/env python3
##
##

attempts = 0
magicWord = 'cisco'
 
while True:
    word = input('Pl enter the magic word :')
    attempts += 1
    if word == magicWord:
        print('You entered the right password in ' + str(attempts) + ' attempts')
        break
    else:
        if attempts == 10: break
        print('No! But you are getting close. You have ' + str(10 - attempts) + ' attempts left')

##
## End of file...
