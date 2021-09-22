##
##
import time
counter = 0

print('Welcome to my Evil Command Center!')
while True:
    try:
        print(counter)
        counter += 1
        time.sleep(1)

    except KeyboardInterrupt:
        print('We will control the veritical.')
        print('We will control the horizontal.')

##
## End of file...
