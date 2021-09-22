##
##
try:
    first = int(input('Enter your first name: '))
    last = input('Enter your last name: ')
except ValueError as valueErrMsg:
    print('Houston, we caught the following exeption: --->' , valueErrMsg)

try:
    print('Your first name is ' + first + ' and your last name is ' + last )
except TypeError as errMessage:
    print('Houston, we caught the following exception: --->', errMessage)

