import os
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#try:
#    f = open('/home/pi/humidity.csv', 'a+')
#    if os.stat('/home/pi/humidity.csv').st_size == 0:
#            f.write('Date,Time,Temperature,Humidity\r\n')
#except:
#    pass

while True:
    h, t = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if h is not None and t is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t,h))
#        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), #time.strftime('%H:%M'), temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    time.sleep(3)
