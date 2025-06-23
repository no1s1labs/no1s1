from datetime import datetime
import serial
from .parse_decode import parse_onelog 

def main_parser():
  initial_date = str(datetime.now()) #if not make into string then it remains as a datetime object
  ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=10)
  output = None
  while output is None:
    try:
      output=parse_onelog(ser)
    except:
      pass
  output["time"]=initial_date
  return(output)



