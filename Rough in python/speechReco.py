import imp
import speech_recognition as sr
from gtts import gTTS
import pyaudio
from playsound import playsound 

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio2 = r.listen(source)

    myText = r.recognize_google(audio2)
    
    myObj = gTTS(myText, lang="en", slow=False)
    myObj.save("audio1.mp3")
    playsound("audio1.mp3")
