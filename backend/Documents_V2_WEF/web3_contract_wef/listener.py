from web3 import Web3,HTTPProvider
from web3.auto import w3
import time


def listen(event):
  allevent_newuser=event.get_all_entries()
  event_value=event.get_new_entries()
  
  while bool(event_value) is False:
    try:
      event_value=event.get_new_entries()
    except KeyboardInterrupt:
      print("user interttupt the process")
      break
  return event_value





  
  

