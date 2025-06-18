import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print("out1 start")
GPIO.setup(17,GPIO.OUT)
#Blue
GPIO.setup(6,GPIO.OUT)
#green
GPIO.setup(22,GPIO.OUT)
#red
time.sleep(1)
print("out1 finish")

print ("gpio17 start")
GPIO.setup(17,GPIO.HIGH)
time.sleep(10)
GPIO.setup(17,GPIO.OUT)
print("gpio17 finish")

print ("gpio6 start")
GPIO.setup(6,GPIO.HIGH)
time.sleep(10)                                                                                                                                                                                                                                                                                                                                             
GPIO.setup(6,GPIO.OUT)
print("gpio6 finish")

print ("gpio22 start")
GPIO.setup(22,GPIO.HIGH)
time.sleep(10)
GPIO.setup(22,GPIO.OUT)
print("gpio22 finish")

except KeyboardInterrupt:
	GPIO.cleanup()
