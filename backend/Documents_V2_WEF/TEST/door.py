#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
print("board set")
#set GPIO Pins
GPIO_DOOR = 24
GPIO_DOOR_DATA = 25

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_DOOR, GPIO.OUT)
GPIO.setup(GPIO_DOOR_DATA, GPIO.IN)
print("pin set")

GPIO.output(GPIO_DOOR, GPIO.LOW)
print('lock closed')
time.sleep(1)
GPIO.output(GPIO_DOOR, GPIO.HIGH)
print('lock on')
time.sleep(1)
GPIO.output(GPIO_DOOR, GPIO.LOW)
print('lock closed')

DOOR_STATUS=GPIO.input(GPIO_DOOR_DATA)
 
if __name__ == '__main__':
    try:
        while True:
            DOOR_STATUS=GPIO.input(GPIO_DOOR_DATA)
            print(DOOR_STATUS)
            time.sleep(2)
            if(DOOR_STATUS==GPIO.LOW):
                print('low')
            if (DOOR_STATUS==GPIO.HIGH):
                print('HIGH')
            else:
            	print("no input")
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Door stopped by User")
        GPIO.cleanup()

