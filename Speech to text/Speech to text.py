import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("ok you can speek now")
    # audio_data = r.record(source, duration= 5)
    audio = r.listen(source)
    print("Recognizing .....")
    text = r.recognize_google(audio)
    print(text)