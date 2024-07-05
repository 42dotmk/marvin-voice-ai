import speech_recognition as sr
from RealtimeTTS import TextToAudioStream, SystemEngine
from gtts import gTTS
import os
from marvin import chat

r = sr.Recognizer()
engine = SystemEngine() 
stream = TextToAudioStream(engine)

def record_text():
    while (1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                text = r.recognize_google(audio)
                return text

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Could not understand audio")


while(1):
    print("Say something!")
    text = record_text()
    text_stream = chat(text)
    stream.feed(text_stream)
    stream.play_async()