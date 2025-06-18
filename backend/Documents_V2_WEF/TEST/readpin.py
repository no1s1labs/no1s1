import time
import RPi.GPIO as GPIO
#from gpiozero import LED
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
print('lock setup')
#GPIO.output(24, 0)
GPIO.output(24, GPIO.LOW)
print('lock closed')



#sleep(4)
try:
	while True:
		input = GPIO.input(12)
		#sleep(3)
		print(input)
		sleep(1)

		if(input==GPIO.LOW):
			print('low')
		if (input==GPIO.HIGH):
			print('HIGH')
		else:
			print('no input')
		
		#sleep(3)
		#GPIO.output(24, 0)
		#print('lock closed')
except KeyboardInterrupt:
	GPIO.cleanup()
	

