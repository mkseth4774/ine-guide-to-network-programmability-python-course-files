##
##
import time
countdown = 10

while True:
    try:
        print('This computer will self destruct in ' + str(countdown) + ' seconds!')
        countdown -= 1
        time.sleep(1)
    except KeyboardInterrupt:
        print("I'm sorry Dave, I'm afraid I can't do that.")

##
## End of file...
