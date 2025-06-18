#common libraries
import time
from time import sleep
import RPi.GPIO as GPIO
from hexbytes import HexBytes
import cv2
#import own modules
from web3_contract import init_contract_wef, txn_blockchain_wef
from door_functions import unlock,lock,howsdoor
from cam_test import cam_detect
from distance_sensor import distance
from led_functions import blink,led_out,one_led_on
from guizero import App, Box, Text, TextBox, Picture, PushButton, TitleBox

#global data
##Contracts
WEFContract,w3=init_contract_wef.start_contract()
##LED pins
Bpin=17 #Blue
Gpin=6 #green
Rpin=22 #red
##other data
global unlocktime
global access_allowtime
global userUUID
##Guizero functions
app = App(title="no1s1", width=500, height=410 )
box = Box(app, align="top", width="fill")
start_button = PushButton(box, command=startcamera, text="Start Camera", align="left")
stop_button = PushButton(box, command=stopcamera, text="Stop Camera", enabled=False,align="right")
pic = Picture(app, image="app.png")
titlebox = TitleBox(app, text="no1s1 Status", layout="grid", width=200, height=75, align="bottom")
doorstatus_label = Text(titlebox, text="Door status: ", size=14, font="Arial",grid=[3,0])
doorstatus = Text(titlebox, text="", size=14, font="Arial",grid=[4,0])
ledtatus_label = Text(titlebox, text="LED status: ", size=14, font="Arial",grid=[3,1])
ledstatus = Text(titlebox, text="", size=14, font="Arial",grid=[4,1])
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
          time.sleep(0.1)
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

def updateStatus():#call this function from different points in the main program 
    print("fetching status")
    doorstatus.value=getdoorStatus()
    ledstatus.value=ledStatus()
    print("Status fetched")

def start_no1s1_listenprogram():#camera on functions
    print("no1s1 listening")
    #STEP 1 
    #prepare the house
    print("start step1, setting up the house")
    GPIO.cleanup()
    GPIO.setwarnings(False)
    print("blink starts")
    led_out()
    one_led_on(Bpin)
    print("lockstarts")
    lock()

def startcamera():
    start_button.disable()
    stop_button.enable()
    updateStatus()
    no1s1_mainProgram()
    updateStatus()


def stopcamera(): #call this function whe you stop the camera function
    start_button.enable()
    stop_button.disable()
    start_no1s1_listenprogram()

def getdoorStatus(): #add code to get the door status
    return "open"
def ledStatus():
    return "ledcolour"

def no1s1_mainProgram(): #add code to get the LED status
    print("Button was pressed")
    #STEP 2
    #check access 
    checkAccessSucceed=False
    while checkAccessSucceed is False:
      try:
          led_out()
          one_led_on(Rpin)
          print("cam_check started")
          cam_data=cam_detect()
          print("data_received is:",cam_data)
          userUUID = cam_data
          print("transaction started")
          txn_hash=txn_blockchain_wef.buy(userUUID)
          transactionSucceed=txn_blockchain_wef.transactionAccess(txn_hash)
          print("transaction hash",txn_hash)
          if transactionSucceed is True:
                  print("access checked successful!")
                  print("wait time 5 seconds")
                  sleep(5)
                  unlock()
                  unlocktime=time.time()
                  print(unlocktime)
                  checkAccessSucceed=True
                  break
          elif transactionSucceed is False:
                  print("something went wrong with the transaction, but I will let you on good will")
                  print("wait time 5 seconds")
                  sleep(5)
                  unlock()
                  unlocktime=time.time()
                  print(unlocktime)
                  checkAccessSucceed=False
                  break
      except KeyboardInterrupt:
          print("user interrupt")
          break
    print("door unlocked at", unlocktime)
    print("user key is", userUUID)
    print("start step3")
    #STEP 3
    #trigger checkactivity to check if people entered
    led_out()
    one_led_on(Gpin)
    entered=disSensorbool()
    if entered is True:
      print("someone enetered space!")
    else: 
      print("sensor did not detect activity, please check with dev") #?#? what is the strategy here?
      #lock()
    print("door unlocked at", unlocktime)
    print("user key is", userUUID)
    print("start step4")
    #STEP3
    #count time from unlock time + allowed time and trigger exit function and strategy 
    allow_time_sec= 90 #access_allowtime *60
    print("allowed time in sec",allow_time_sec)
    user_exit = unlocktime + allow_time_sec
    print("exit time",user_exit)
    led_out()
    one_led_on(Bpin)
    while True:
      print("wait for user to settle in")
      sleep(5)
      door_status=howsdoor()
      print("door status is",door_status)
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
            led_out()
            one_led_on(Rpin)
            #?#? cause a buzz? or a little speaker?
          else:
            user_exit_self=time.time()
            unlock()
            _dooropened = True
            #?#? LATER add additional door status listening (while doing lock and unlock)
            _actualDuration = int((user_exit_self - unlocktime)/60)
            print("actual duration is", _actualDuration)
            print("user key is", userUUID)
            txn_hash_exit=txn_blockchain_wef.exit(_dooropened,int(_actualDuration),userUUID)
            exit_txn_Succeed=txn_blockchain_wef.transactionAccess(txn_hash_exit)
            lock()
            break
      elif(door_status == 1):
            print("door is unlocked by the user")
            user_exit = time.time()
            _actualDuration = int((user_exit - unlocktime)/60)
            _dooropened=True
            print("actual duration is", _actualDuration)
            print("user key is", userUUID)
            txn_hash_exit=txn_blockchain_wef.exit(_dooropened,_actualDuration,userUUID)
            exit_txn_Succeed=txn_blockchain_wef.transactionAccess(txn_hash_exit)
            lock()
            break
      elif(door_status == 2):
            print("error occured, no input")
            unlock()
            break


app.display()
start_no1s1_listenprogram()


# ##--------------------------##
# ##--------------------------##
# ##--------------------------##
# #STEP 1
# #prepare the house
# print("start step1, setting up the house")
# GPIO.cleanup()
# GPIO.setwarnings(False)
# print("blink starts")
# led_out()
# one_led_on(Bpin)
# print("lockstarts")
# lock()

# #STEP 2
# #Listen to buy event emit and catch the key
# print("start step2: listening")
# #prepare newQRcode event
# event_key = DataContract.events.newQRcode.createFilter(fromBlock=0)
# #call module listener and listen function, return key value 
# returned_EKvalue=listener.listen(event_key)
# print(returned_EKvalue)

# #?#? NOT WORKING extract qr value and decode
# #key_value=returned_EKvalue[0]['args'] 
# #decoded_qr=HexBytes.hex(key_value['qrCode'])
# #print("user key is",decoded_qr)

# checkAccessSucceed=False
# while checkAccessSucceed is False:
#   try:
#    led_out()
#    one_led_on(Rpin)
#    print("cam_check started")
#    cam_data=cam_detect()
#    print("data_received is:",cam_data)
#    userUUID = cam_data
#    print("transaction started")
#    txn_hash=txn_blockchain.access(userUUID)
#    transactionSucceed=txn_blockchain.transactionAccess(txn_hash)
#    print("transaction hash",txn_hash)
#    if transactionSucceed is True:
#           print("access checked successful!")
#           print("wait time 5 seconds")
#           sleep(5)
#           unlock()
#           unlocktime=time.time()
#           print(unlocktime)
#           checkAccessSucceed=True
#           break
#    elif transactionSucceed is False:
#           print("something went wrong with the transaction, please input it manully")
#           print("now i am waiting")
#           access_value_bool=False
#           while access_value_bool is False:
#             try:
#               event_access=DataContract.events.accessSuceeded.createFilter(fromBlock=0)
#               returned_EAvalue=listener.listen(event_key)
#               access_value_dict=returned_EAvalue[0]['args']
#               access_value_bool=access_value_dict['success']
#               access_allowtime=access_value_dict['allowedTime']
#               #?#?check if these are currect
#             except:
#               pass
#           print("wait time 5 seconds")
#           sleep(5)
#           unlock()
#           unlocktime=time.time()
#           print(unlocktime)
#           checkAccessSucceed=False
#           break
#   except KeyboardInterrupt:
#    print("user interrupt")
#    break
# print("door unlocked at", unlocktime)
# print("user key is", userUUID)
# print("start step3")
# #STEP3
# #trigger checkactivity to check if people entered
# led_out()
# one_led_on(Gpin)
# entered=disSensorbool()
# if entered is True:
#    print("someone enetered space!")
#    print("starts transaction")
#    while True:
#      try:
#        txn_hash_activity=txn_blockchain.activity(entered,userUUID)
#        activity_transactionSucceed=txn_blockchain.transactionAccess(txn_hash_activity)
#        if activity_transactionSucceed is True:
#          print("user activity transation successful!")
#          lock()
#          break
#        else: 
#          print("user activity transaction unsuccessfully,try again")
#      except KeyboardInterrupt:
#        print("user ended transaction")
# else: 
#    print("sensor did not detect activity, your money is lost?") #?#? what is the strategy here?
#    lock()
# print("door unlocked at", unlocktime)
# print("user key is", userUUID)
# print("start step4")
# #STEP3
# #count time from unlock time + allowed time and trigger exit function and strategy 
# ##!! allowed time captured by emit! actually
# #now=time.time()
# #print("now",now)
# #unlocktime= now - 30
# allow_time_sec= 60 #access_allowtime *60
# print("allowed time in sec",allow_time_sec)
# user_exit = unlocktime + allow_time_sec
# print("exit time",user_exit)
# led_out()
# one_led_on(Bpin)
# while True:
#    print("wait for user to settle in")
#    sleep(5)
#    door_status=howsdoor()
#    print("door status is",door_status)
#    current_countingexit=time.time()
#    remaining_time = user_exit - current_countingexit 
#    print("remaintime",remaining_time)
#    if door_status == 0: #door remain locked
#        if current_countingexit < (user_exit - 15):
#          _dooropened=False
#          sleep(0.5)
#          print("enjoy your meditation")
#        if current_countingexit < (user_exit - 5):
#          _dooropened=False
#          sleep(0.5)
#          print("meditation finish in " + str(int(user_exit-current_countingexit))  + " seconds")
#          led_out()
#          one_led_on(Rpin)
#          #?#? cause a buzz? or a little speaker?
#        else:
#          user_exit_self=time.time()
#          unlock()
#          _dooropened = True
#          #?#? LATER add additional door status listening (while doing lock and unlock)
#          _actualDuration = int((user_exit_self - unlocktime)/60)
#          print("actual duration is", _actualDuration)
#          print("user key is", userUUID)
#          txn_hash_exit=txn_blockchain.exit(_dooropened,int(_actualDuration),userUUID)
#          exit_txn_Succeed=txn_blockchain.transactionAccess(txn_hash_exit)
#          lock()
#          break
#    elif(door_status == 1):
#          print("door is unlocked by the user")
#          user_exit = time.time()
#          _actualDuration = int((user_exit - unlocktime)/60)
#          _dooropened=True
#          print("actual duration is", _actualDuration)
#          print("user key is", userUUID)
#          txn_hash_exit=txn_blockchain.exit(_dooropened,_actualDuration,userUUID)
#          exit_txn_Succeed=txn_blockchain.transactionAccess(txn_hash_exit)
#          lock()
#          break
#    elif(door_status == 2):
#          print("error occured, no input")
#          unlock()
#          break
