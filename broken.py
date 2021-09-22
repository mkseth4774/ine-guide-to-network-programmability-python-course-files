##
##
import logging
logging.basicConfig(filename='pythonlog.log', 
                    filemode='w', 
                    level=logging.INFO, 
                    format='%(levelname)s:%(asctime)s:%(message)s',
                    datefmt='%m.%d.%Y___%H:%M:%S')

def sum(a, b):
    logging.info('We received %s and %s into the sum() function: ', a, b) 
    print('The sum of those numbers is: ', a + b)

def product(x, y):
    logging.info('We received %s and %s into the product() function: ', x, y) 
    print('The product of those numbers is: ', x * y)

def main():
    logging.debug('We are not going to see this!!!')
    var1 = int(input('Enter a positive integer: '))
    var2 = int(input('Enter another positive integer: '))
    sum(var1, var2)
    product(var1, var2)

if __name__ == '__main__':
    main()
##
## End of file...
