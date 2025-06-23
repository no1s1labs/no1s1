import time
import contract_inst_uuid_gas
import cv2
from time import sleep
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

t_cam_end = time.time() +30*1 # 1 minute loop
t_door=time.time()+15*1
t_blink=time.time()+8*1

gled=22
rled=17
bled=6

def camcheck():
 global uuid
 uuid=contract_inst_uuid_gas.retrive_useruuid()
 #print(uuid)
 global data
 while time.time()<t_cam_end:
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    # get the image
    _, img = cap.read()
    # get bounding box coords and data
    data, bbox, _ = detector.detectAndDecode(img)
    #print(data)
    if data:
       break
    # display the image preview
    #cv2.imshow("code detector", img)

# free camera object and exit
    cap.release()
    #cv2.destroyAllWindows()
 #print(data)


def unlockdoor():
 door = LED(24)
 while time.time()<t_door:
    door.on()
    print("Door unlocked")
    sleep(1)
    door.off()
    
def blink(pin):
	GPIO.setup(pin,GPIO.OUT)
	pwm=GPIO.PWM(pin,100)
	pwm.start(0)
	while time.time()<t_blink:
		for x in range(100):
			pwm.ChangeDutyCycle(x)
			sleep(0.01)
				
		for x in range(100,0,-1):
			pwm.ChangeDutyCycle(x)
			sleep(0.01)
	pwm.stop()
	GPIO.setup(pin,GPIO.OUT)

camcheck()
print ("camera qr scan:",data)
print("retrieved uuid:",uuid)
if (int(data) == int(uuid)):
 print("data matched")
 blink(rled)
 unlockdoor()
else:
 print("data not matched")
#while True:
#	if data == uuid:
#		print("data matched!")


