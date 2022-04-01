# import RPi.GPIO as GPIO
import time
import speech_recognition as sr
import pyttsx3
import os
import sys

r = sr.Recognizer()
mic = sr.Microphone()
engine = pyttsx3.init()

led_alarm = 18
buzzer_alarm = 31

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(led_alarm, GPIO.OUT)
# GPIO.setup(buzzer_alarm, GPIO.OUT)

#set two voices, indext 0 for male and 1 for female
voices = engine.getProperty("voices")
print("male voice: {0}". format(voices[0].id))
print("female voice: {0}". format(voices[1].id))

""" 
the next thing to do is to set up a wake up word!!!
"""

while True:
    with mic as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        
        #set voice to be used
        engine.setProperty("voice", voices[0].id)

        print("ok you can speek now")
        audio_data = r.listen(source)

        
        try:
            print("Recognizing .....")
            text = r.recognize_google(audio_data)
            if "soma" in text:
                print(text)
                engine.say(text)
                engine.runAndWait()
            
        except sr.UnknownValueError:
            err = "don't know what you said"
            engine.say(err)
            engine.runAndWait()
            print(err)

        except sr.RequestError as e:
            requesterror = "unable to request result from Google Speech Recognition Server:{}".format(e)
            print (requesterror)
            engine.say(requesterror)
            engine.runAndWait()