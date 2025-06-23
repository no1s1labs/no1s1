#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

GPIO_DOOR = 24
GPIO_DOOR_DATA = 25

#set GPIO direction (IN / OUT)
#GPIO.setup(GPIO_DOOR, GPIO.OUT)
#GPIO.setup(GPIO_DOOR_DATA, GPIO.IN)

def unlock():
 GPIO.cleanup()
 GPIO.setmode(GPIO.BCM)
 GPIO_DOOR = 24
 GPIO_DOOR_DATA = 25
 GPIO.setup(GPIO_DOOR, GPIO.OUT)
 GPIO.output(GPIO_DOOR, GPIO.HIGH)

def lock():
 GPIO.cleanup()
 GPIO.setmode(GPIO.BCM)
 GPIO_DOOR = 24
 GPIO_DOOR_DATA = 25
 GPIO.setup(GPIO_DOOR, GPIO.OUT)
 GPIO.output(GPIO_DOOR, GPIO.LOW)
 
def howsdoor():
 GPIO.setmode(GPIO.BCM)
 GPIO_DOOR = 24
 GPIO_DOOR_DATA = 25
 GPIO.setup(GPIO_DOOR_DATA, GPIO.IN)
 DOOR_STATUS=GPIO.input(GPIO_DOOR_DATA)
 if(DOOR_STATUS==GPIO.LOW):
   return 0
   print('LOW,lock')
 if (DOOR_STATUS==GPIO.HIGH):
   return 1
   print('HIGH,unlock')
 else:
   return 2
   print("no input")

# the logic: if the time is still 
