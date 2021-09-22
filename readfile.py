##
## readfile.py
##
def readFile(filename):
	try:
		f = open(filename)
		fullFile = f.read()
		print(fullFile.strip())
	except FileNotFoundError as fileError:
		print('Error Caught: ---> ', fileError)
	finally:
		print('WE ARE IN THE FINALLY BLOCK OF CODE!!!')
		try:
			f.close()
		except UnboundLocalError as localError:
			print('Error was: ---> ', localError)

def main():
	filename = input('Enter file name: ')
	readFile(filename)

if __name__ == '__main__':
	main()

##
## End of file...