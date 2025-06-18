cs = {
    0: 'Not charging',
    2: 'Fault',
    3: 'Bulk',
    4: 'Absorption',
    5: 'Float'
    }

err = {
    0: 'No error',
    2: 'Battery voltage too high',
    3: 'Remote temperature sensor failure',
    4: 'Remote temperature sensor failure',
    5: 'Remote temperature sensor failure (connection lost)',
    6: 'Remote battery voltage sense failure',
    7: 'Remote battery voltage sense failure',
    8: 'Remote battery voltage sense failure (connection lost)',
    17: 'Charger temperature too high',
    18: 'Charger over current',
    19: 'Charger current reversed',
    20: 'Bulk time limit exceeded',
    21: 'Current sensor issue (sensor bias/sensor broken)',
    26: 'Terminals overheated',
    28: 'Power stage issue',
    33: 'Input voltage too high (solar panel)',
    34: 'Input current too high (solar panel)',
    38: 'Input shutdown (due to excessive battery voltage)',
    39: 'Input shutdown',
    65: '[Info] Communication warning',
    66: '[Info] Incompatible device',
    67: 'BMS Connection lost',
    114: 'CPU temperature too high',
    116: 'Factory calibration data lost',
    117: 'Invalid/incompatible firmware',
    119: 'User settings invalid'
    }

mppt = {
    0: 'Off',
    1: 'Voltage or current limited',
    2: 'MPP Tracker active'
    }

def converter(packet,conv):
    try:
        if conv == "cs":
            return cs[int(packet)]
        if conv == "err":
            return err[int(packet)]
        if conv == "mppt":
            return mppt[int(packet)]
    except:
        print("[!] Unrecognised value type of",conv,":",packet)
        return packet


def parse_onelog(ser):
  global elec_data
  elec_data = {}

  while True:
    #print(ser)
    ve_read = ser.readline()
    decoded_str=ve_read.decode("utf-8")
    #return decoded_str
    #print(ve_read)
    #print(decoded_str)
    
    #= Product ID =#      
    if "PID" in decoded_str: 
      split_data = decoded_str.split("\t")
      strip_data = split_data[1]
      product_id=strip_data.replace("\r\n","")
      #print("product id")
      #print(product_id)
      elec_data["productid"]=product_id
    #= Firmware Version =#
    elif "FW" in decoded_str:
      split_data = decoded_str.split("\t")
      strip_data = split_data[1]
      product_fw=strip_data.replace("\r\n","")
      #print("fw",product_fw)
      elec_data["fw"]=product_fw
    #= Serial number =#
    elif "SER" in decoded_str:
      split_data = decoded_str.split("\t")
      strip_data = split_data[1]
      product_ser=strip_data.replace("\r\n","")
      elec_data["serial"]=product_ser
    #= Battery voltage =#
    elif "V" in decoded_str and "P" not in decoded_str: #For VPV and PPV cases
      split_data = decoded_str.split("\t")
      batteryV=float(split_data[1])*0.001
      elec_data["batteryV"]=batteryV

    #= Current =#
    elif "I" in decoded_str and "P" not in decoded_str: #For PID cases
      split_data = decoded_str.split("\t")
      batteryC=float(split_data[1])*0.001
      elec_data["batteryC"]=batteryC

    #= PV Voltage =#
    elif "VPV" in decoded_str:
      split_data = decoded_str.split("\t")
      pvV=float(split_data[1])*0.001
      elec_data["pvV"]=pvV

    #= PV Power =#
    elif "PPV" in decoded_str:
      split_data = decoded_str.split("\t")
      pvP=int(split_data[1])
      elec_data["pvP"]=pvP

    #= State of operation =#
    elif "CS" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = converter(int(split_data[1]),"cs")
      elec_data["StateofOperation"]=packet

    #= Tracker operation mode =#
    elif "MPPT" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = converter(int(split_data[1]),"mppt")
      elec_data["MPPTMode"]=packet

    #= Error code =#
    elif "ERR" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = converter(int(split_data[1]),"err")
      elec_data["error"]=packet

    #= Load otput state (ON/OFF) =#
    elif "LOAD" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = (split_data[1]).replace("\r\n","")
      elec_data["sysload"]=packet

    #= Yield total =#
    elif "H19" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = float(split_data[1]) * 0.01
      elec_data["yieldTotal"]=packet

    #= Yield today =#
    elif "H20" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = float(split_data[1]) * 0.01
      elec_data["yieldToday"]=packet

    #= Maximum power today =#
    elif "H21" in decoded_str:
            split_data = decoded_str.split("\t")
            packet = float(split_data[1])
            elec_data["maxPower"]=packet

    #= Yield yesterday =#
    elif "H22" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = float(split_data[1]) * 0.01
      elec_data["yieldYst"]=packet

    #= Maximum power yesterday =#
    elif "H23" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = float(split_data[1])
      elec_data["maxPowerYst"]=packet

    #= Day sequence number (0..364) =#
    elif "HSDS" in decoded_str:
      split_data = decoded_str.split("\t")
      packet = int(split_data[1])
      elec_data["daySeqNo"]=packet
      return elec_data

    # #= Checksum =#
    # elif "Checksum" in decoded_str:
    #     print("Checksum identified. Reader progress:",line)
    #     time.sleep(1)
    #     line = line + 1     #Go to next line in xls (Checksum is last value)

    # #= NULL =#
    # else:
    #     print("[!] Unrecognised data:",decoded_line)
      
      
      
     
  #except:
     #print("can't decode anymore")
     #return elec_data
     # return decoded_str,product_id

