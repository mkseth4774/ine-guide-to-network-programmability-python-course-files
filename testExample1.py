#!/usr/bin/env python3
##
##

attempts = 0
magicWord = 'cisco'
boolPassword = False
 
while not boolPassword:
    if attempts > 4: break
    word = input('Pl enter the magic word :')
    attempts += 1
    if word != magicWord: 
        print('No! But you are getting close. You have ' + str(5 - attempts) + ' attempts left')
        continue
    else:
        boolPassword = True
else:
    print('This part of the code gets executed')
    if boolPassword == True:
        print('Good Job You entered the right password in ' + str(attempts) + ' attempts')
    else:
        print('Better luck next time')

print(boolPassword)
##
## End of file...
