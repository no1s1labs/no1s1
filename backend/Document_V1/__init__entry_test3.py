#common libraries
import time
from time import sleep
import RPi.GPIO as GPIO
from hexbytes import HexBytes
import cv2
#import own modules
##please rename web3 to avoid confusion!!!!!
from web3_contract import listener, init_contract, txn_blockchain
##please rename web3 to avoid confusion!!!!!
from door_functions import unlock,lock,howsdoor
from cam_test import cam_detect
from distance_sensor import distance
from led_functions import blink,led_out,one_led_on


#global data
##Contracts
AppContract,DataContract,w3=init_contract.start_contract()
##LED pins
Bpin=17 #Blue
Gpin=6 #green
Rpin=22 #red
##other data
global unlocktime
global access_allowtime
#global functions 
def disSensorbool():
    sensor_start_time=time.time()
    print("start time",sensor_start_time)
    sensor_duration=30*1
    sensor_end_time=sensor_start_time+sensor_duration
    print("end_time",sensor_end_time)
    while True:
      current_time=time.time()
      print("current time",current_time)
      elapsed_time=current_time-sensor_start_time
      if current_time < sensor_end_time:
          print("sensor started: " + str(int(elapsed_time))  + " seconds")
          print("sensor endes: " + str(int(sensor_duration-elapsed_time))  + " seconds")
          dist = distance()
          #print (dist)
          #print ("Measured Distance = %.1f cm" % dist) #onedecimal
          time.sleep(1)
          #print(int(dist))
          if int(dist) in range(60,86):
            #print ("door is closed")
            someoneEntered= False
          elif int(dist) > 86 :
            #print("door is opened")
            someoneEntered= False
          elif int(dist) < 60 : 
            print("someone entered")
            return True
      else:
        print("no one entered")
        return False

#print("distance loop starts")
#returned=disSensorbool()
#print(returned)

#STEP 1
#STEP 1.1
#Listen to buy event emit and catch the key
#prepare the house
GPIO.cleanup()
GPIO.setwarnings(False)

print("start step3")

# #STEP3
# #count time from unlock time + allowed time and trigger exit function and strategy 
# ##!! allowed time captured by emit! actually
lock()
now=time.time()
print("now",now)
unlocktime= now - 30
print("unlocktime",unlocktime)
allow_time_sec= 60 #access_allowtime *60
user_exit = unlocktime + allow_time_sec
print("exit time",user_exit)
led_out()
one_led_on(Bpin)

while True:
   door_status=howsdoor()
   print(door_status)
   current_countingexit=time.time()
   remaining_time = user_exit - current_countingexit 
   print("remaintime",remaining_time)
   if door_status == 0: #door remain locked
       if current_countingexit < (user_exit - 15):
         _dooropened=False
         sleep(0.5)
         print("enjoy your meditation")
       if current_countingexit < (user_exit - 5):
         _dooropened=False
         sleep(0.5)
         print("meditation finish in " + str(int(user_exit-current_countingexit))  + " seconds")
         #?#? cause a buzz? or a little speaker?
       else:
         user_exit_self=time.time()
         unlock()
         _dooropened = True
         #?#? add additional door status listening (while doing lock and unlock)
         _actualDuration = user_exit_self - unlocktime
         #fake
         key_value="0xbd387b512a9d8717f6d58b89866880bf1bef6aee15b1f65b613f4f0f5857d108"
         txn_hash_exit=txn_blockchain.exit(_dooropened,int(_actualDuration),key_value)
         exit_txn_Succeed=txn_blockchain.transactionAccess(txn_hash_exit)
         break
   elif(door_status == 1):
         print("door is unlocked by the user")
         user_exit = time.time()
         _actualDuration = int(user_exit - unlocktime)
         _dooropened=True
         key_value="0xbd387b512a9d8717f6d58b89866880bf1bef6aee15b1f65b613f4f0f5857d108"
         print(key_value)
         #txn_hash_exit=txn_blockchain.exit(_dooropened,_actualDuration,key_value)
         txn_hash_exit=txn_blockchain.exit(True,10,"0xbd387b512a9d8717f6d58b89866880bf1bef6aee15b1f65b613f4f0f5857d108")
         exit_txn_Succeed=txn_blockchain.transactionAccess(txn_hash_exit)
         break
   elif(door_status == 2):
         print("error occured, no input")
         unlock()
         break


