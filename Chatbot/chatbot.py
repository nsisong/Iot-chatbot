import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("ok you can speek now")
    audio_data = r.record(source, duration= 5)
    print("Recognizing .....")
    text = r.recognize_google(audio_data)
    print(text)
    engine.say(text)
    engine.runAndWait()