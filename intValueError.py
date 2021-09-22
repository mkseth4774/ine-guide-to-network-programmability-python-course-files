##
##
try:
    number = int(input('Please enter a number: '))
    print('You entered: ', number)
except ValueError as errMessage:
    print('You need to enter an integer! -->', errMessage)
