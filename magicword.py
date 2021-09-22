#!/usr/bin/env python3
##
##
attempts = 0
magicWord = 'cisco'

while True:
    word = input('Please enter the magic word: ')
    attempts += 1
    if word == magicWord:
        break
    else:
        print('No, but you are getting closer!')

print('You just exited the loop!!!')
print('Congratulations, you guessed the magic word in ' + str(attempts) + ' trys!!!')
##
##
##End of file
