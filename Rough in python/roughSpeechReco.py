from fileinput import filename
from operator import gt
import playsound 
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save("voice.mp3")
    playsound.playsound(filename)

def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: "+str(e))
        
    return said

# speak("Hello World")
getAudio()