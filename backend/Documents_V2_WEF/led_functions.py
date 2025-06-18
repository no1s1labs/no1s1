import RPi.GPIO as GPIO
import time
from time import sleep

def blink(pin,sleeptime):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	pwm=GPIO.PWM(pin,100)
	try:
		pwm.start(0)
		while True:
			for x in range(100):
				pwm.ChangeDutyCycle(x)
				sleep(sleeptime)
					
			for x in range(100,0,-1):
				pwm.ChangeDutyCycle(x)
				sleep(sleeptime)
		pwm.stop()
	except Exception as e:
		print(e)
	GPIO.setup(pin,GPIO.OUT)

def led_out():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17,GPIO.OUT)
	GPIO.setup(6,GPIO.OUT)
	GPIO.setup(22,GPIO.OUT)
	GPIO.output(17,GPIO.LOW)
	GPIO.output(6,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	
def one_led_on(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)

def one_led_off(pin):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin,GPIO.OUT)
	GPIO.output(pin,GPIO.HIGH)

