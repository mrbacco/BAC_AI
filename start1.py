# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 09:58:43 2022

@author: mrbac
"""

import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence
from pathlib import Path

##### OS VARIABLES START #####
path = Path().absolute() # Directory of current working directory
path_file = Path(__file__).absolute() # file to use within the directory
print("File      Path:", path_file)
print("Directory Path:", path)
##### OS VARIABLES END ##### 

##### OPENING A FILE AND RECORDING START #####
file = "rec002.wav"
result = open("recognized.txt", "a")

# initialize the recognizer
r = sr.Recognizer()

# opening the wav file and writing the content into a text file
with sr.AudioFile(file) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data, language = "en_US")
    # dumping content into a text file and close it
    result.write("\n")
    result.write("\n")
    result.write(text)
    result.close()
    print(text)

##### OPENING A FILE AND RECORDING END #####

##### SENTIMENT ANALYSIS OF TEXT START #####


##### SENTIMENT ANALYSIS OF TEXT END #####
