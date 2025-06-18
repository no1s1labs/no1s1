from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	print("waiting for signal")
	pir.wait_for_motion()
	print("You moved")
	pir.wait_for_no_motion()
	print("no movement")
	
	
