import RPi.GPIO as GPIO

channel = 16
GPIO.setmode(GPIO.BCM)  
# Setup your channel
GPIO.setup(channel, GPIO.OUT)
#GPIO.output(channel, GPIO.LOW)

# To test the value of a pin use the .input method
channel_is_on = GPIO.input(channel)  # Returns 0 if OFF or 1 if ON

if channel_is_on:
	print ('is on')
else: 
	print('is off')
    # Do something here
