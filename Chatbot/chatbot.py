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

with mic as source:
    r.adjust_for_ambient_noise(source)
    
    #set two voices, indext 0 for male and 1 for female
    voices = engine.getProperty("voices")
    print("male voice: {0}". format(voices[0].id))
    print("female voice: {0}". format(voices[1].id))

    #set voice to be used
    engine.setProperty("voice", voices[0].id)

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
        err = "don't know what you said"
        engine.say(err)
        engine.runAndWait()
        print(err)

    except sr.RequestError as e:
        requesterror = "unable to request result from Google Speech Recognition Server:{}".format(e)
        print (requesterror)
        engine.say(requesterror)
        engine.runAndWait()