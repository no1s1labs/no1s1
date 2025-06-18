#Libraries
import RPi.GPIO as GPIO
import time
 



 
def distance():
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)
    print("board set")
    #set GPIO Pins
    GPIO_TRIGGER = 23
    GPIO_ECHO = 26
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    print("pin set")
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    #print("trigger set to high")
    # set Trigger after 0.01ms to LOW
    time.sleep(0.01)#0.00001
    GPIO.output(GPIO_TRIGGER, False)
    #print("trigger set to low")
 
    StartTime = time.time()
    StopTime = time.time()
    #print("start time")
    #print(StartTime)
    #print("stop time")
    #print(StopTime)

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        #print("input 0")
        #print(StartTime)

 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        #print("input 1")
        #print(StopTime)
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    #print(distance)
 
    return distance
 

