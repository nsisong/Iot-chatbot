import RPi.GPIO as GPIO
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

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_alarm, GPIO.OUT)
GPIO.setup(buzzer_alarm, GPIO.OUT)

with mic as source:
    r.adjust_for_ambient_noise(source)
    print("ok you can speek now")
    # audio_data = r.record(source, duration= 5)
    audio_data = r.listen(source)
    
    try:
        print("Recognizing .....")
        text = r.recognize_google(audio_data)
        print(text)
        engine.say(text)
        engine.runAndWait()
        
    except sr.UnknownValueError:
        print("don't know what you said")

    except sr.RequestError as e:
        print ("unable to request result from Google Speech Recognition Server:{}".format(e))