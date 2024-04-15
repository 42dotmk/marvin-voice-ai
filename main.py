import speech_recognition as sr
from gtts import gTTS 
import os

r = sr.Recognizer()


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


def output_text(text):
    f = open("output.txt", "w")
    f.write(text)
    f.write("\n")
    f.close()
    return


def speak_text(text):
    speechFile = gTTS(text=text, tld='ie', lang='en', slow=False)
    speechFile.save("speech.mp3")
    os.system("mpg321 speech.mp3")

while (1):
    text = record_text()
    output_text(text)
    speak_text(text)

    print(text)
