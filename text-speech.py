# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
  
# This module is imported so that we can  
# play the converted audio 
import os 

mytext  = input("")

language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("a.mp3") 
  
# Playing the converted file 
os.system("a.mp3")
