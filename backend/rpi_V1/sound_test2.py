#from num2words import num2words
from subprocess import call
import time

def playsound():

  cmd_beg= 'aplay '
  cmd_end= ' /home/no1s1/Downloads/test.wav  ' # To play back  the stored .wav file and to dump the std errors to /dev/null


  #Calls the Espeak TTS Engine to read aloud a Text
  call([cmd_beg+cmd_end], shell=True)
  
def stopsound():
  process = subprocess.Popen(cmd, shell=True)
  process.terminate()
  
  
playsound()
time.sleep(5)
stopsound()
