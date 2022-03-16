import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("ok you can speek now")
    audio_data = r.record(source, duration= 10)
    print("Recognizing .....")
    text = r.recognize_google(audio_data)
    print(text)