##
## division.py
##
def division(x, y):
	try:
		result = x // y
	except ZeroDivisionError as divisionError:
		print('No, you still cannot divide by zero (0)!')
		print('Error Caught: ---> ', divisionError)
	except KeyboardInterrupt as myKeyboard:
		print('You must use integers!')
		print('Error Caught: ---> ', myKeyboard)
	else:
		print(result)

def main():

    x = int(input('Enter a value for x: '))
    y = int(input('Enter a value for y: '))
    
    division(x, y)

if __name__ == '__main__':
	main()

##
## End of file...