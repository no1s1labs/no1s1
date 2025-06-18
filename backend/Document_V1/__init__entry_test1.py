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
print("blink starts")
led_out()
one_led_on(Bpin)
print("lockstarts")
lock()

print("start listening")
##prepare newQRcode event
#event_key = DataContract.events.newQRcode.createFilter(fromBlock=0)
##call module listener and listen function, return key value 
#returned_EKvalue=listener.listen(event_key)
#print(returned_EKvalue)

#key_value=returned_EKvalue[0]['args'] #?#?is this also true to newQRcode event??TEST
#decoded_qr=HexBytes.hex(key_value['qrCode'])
#print(key_value)
checkAccessSucceed=False
while checkAccessSucceed is False:
  try:
   led_out()
   one_led_on(Rpin)
   print("cam_check started")
   #cam_data=cam_detect()
   #print("data_received is:",cam_data)
   #userUUID = cam_data
   userUUID = "0xbd387b512a9d8717f6d58b89866880bf1bef6aee15b1f65b613f4f0f5857d108"
   print("transaction started")
   txn_hash=txn_blockchain.access(userUUID)
   transactionSucceed=txn_blockchain.transactionAccess(txn_hash)
   print("transaction hash",txn_hash)
   if transactionSucceed is True:
          print("access checked successful!")
          unlock()
          unlocktime=time.time()
          print(unlocktime)
          checkAccessSucceed=True
          break
   elif transactionSucceed is False:
          print("something went wrong with the transaction, please input it manully")
          print("now i am waiting")
          access_value_bool=False
          while access_value_bool is False:
            try:
              event_access=DataContract.events.accessSuceeded.createFilter(fromBlock=0)
              returned_EAvalue=listener.listen(event_key)
              access_value_dict=returned_EAvalue[0]['args']
              access_value_bool=access_value_dict['success']
              access_allowtime=access_value_dict['allowedTime']
              #?#?check if these are currect
            except:
              pass
          unlock()
          unlocktime=time.time()
          print(unlocktime)
          checkAccessSucceed=False
          break
  except KeyboardInterrupt:
   print("user interrupt")
   break
#cap.release()
#cv2.destroyAllWindows()
#!!!!!!! change the logic here to just return successful transaction
# #STEP 1.2
# #open camera and get raeding from QRcode and check access
# ##turn on camera and check qrcode
# checkAccessSucceed=False
# while checkAccessSucceed is False:
#   try:
#     led_out()
#     blink(Rpin,0.01) 
#     cam_data=camcheck() #?#? the timeline here, the camera is on for 3 minutes?
#     #STEP 1.3
#     #check if userdata match the key data
#     #match then trigger checkaccess and open door
#     #?#?what is the data type of cam_data and key_value, could cause error
#     if cam_data == key_value:
#       userUUID = cam_data
#       #?#? add a emit catcher here so that the people are listening to it!!!
#       txn_hash=txn_blockchain.access(userUUID)
#       transactionSucceed=txn_blockchain.transactionAccess(txn_hash)
#       if transactionSucceed is True:
#         print("access checked successful!")
#         unlock()
#         unlocktime=time.time()
#         print(unlocktime)
#         break
#       elif transactionSucceed is False:
#         print("something went wrong with the transaction, please input it manully")
#         print("now i am waiting")
#         access_value_bool=False
#         while access_value_bool is False:
#           try:
#             event_access=DataContract.events.accessSuceeded.createFilter(fromBlock=0)
#             returned_EAvalue=listener.listen(event_key)
#             access_value_dict=returned_EAvalue[0]['args']
#             access_value_bool=access_value_dict['success']
#             access_allowtime=access_value_dict['allowedTime']
#             #?#?check if these are currect
#           except:
#             pass
#         unlock()
#         unlocktime=time.time()
#         print(unlocktime)
#         break
#         #!#! add a loop that retrive the no1s1 occupancy status or listen to accessSuceeded(true, allowedDuration);
#     else: 
#       print("camera data do not match emit value")
#       print("camera reads",cam_data)
#       print("key emitted by smart contract",userUUID)
#       print("scan again?")
#       #?#?is this line neccesarry?
#       #cam_data=camcheck()
#   except KeyboardInterrupt:
#     print("user stopped it")

# #STEP2
# #trigger checkactivity to check if people entered
# led_out()
# blink(Gpin,1)
# entered=disSensorbool()
# if entered is True:
#   print("someone enetered space!")
#   print("starts transaction")
#   while True:
#     try:
#       txn_hash_activity=txn_blockchain.activity(entered,key_value)
#       activity_transactionSucceed=txn_blockchain.transactionAccess(txn_hash_activity)
#       if activity_transactionSucceed is True:
#         print("user activity transation successful!")
#         lock()
#         break
#       else: 
#         print("user activity transaction unsuccessfully,try again")
#     except KeyboardInterrupt:
#       print("user ended transaction")
# else: 
#   print("sensor did not detect activity, your money is lost?") #?#? what is the strategy here?
#   lock()
# #STEP3
# #count time from unlock time + allowed time and trigger exit function and strategy 
# ##!! allowed time captured by emit! actually
# allow_time_sec= access_allowtime *60
# user_exit = unlocktime + allow_time_sec
# current_coutingexit=time.time()
# remaining_time = user_exit - current_coutingexit 

# while remaining_time >0:
#   led_out()
#   blink(Bpin,1)
#   door_status=howsdoor()
#   while door_status == 0: #door remain locked
#     try:
#       if remaining_time > 15:
#         _dooropened=False
#         print("enjoy your meditation")
#       if remaining_time > 5:
#         _dooropened=False
#         print("meditation finish in " + str(int(remaining_time))  + " seconds")
#         #?#? cause a buzz? or a little speaker?
#       else:
#         user_exit=time.time()
#         unlock()
#         _dooropened = True
#         #?#? add additional door status listening (while doing lock and unlock)
#         _actualDuration = user_exit - unlocktime
#         txn_hash_exit=txn_blockchain.exit(_dooropened,_actualDuration,key_value)
#         exit_txn_Succeed=txn_blockchain.transactionAccess(txn_hash)
#     except:
#       if(door_status == 1):
#         print("door is unlocked by the user")
#         user_exit = time.time()
#         _actualDuration = user_exit - unlocktime
#         _dooropened=True
#         txn_hash_exit=txn_blockchain.exit(_dooropened,_actualDuration,key_value)
#         exit_txn_Succeed=txn_blockchain.transactionAccess(txn_hash)
#       if(door_status == 2):
#         print("error occured, no input")
#         unlock()


