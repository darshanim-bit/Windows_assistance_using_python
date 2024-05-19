import speech_recognition as sr
import pyttsx4 as tts
import datetime
import wikipedia
import webbrowser
import os


# Taking Voice From my system
   
engine = tts.init()
voices = engine.getProperty('voices')
# print([voice.id for voice in voices])
engine.setProperty('voice',voices[0].id)
# engine.setProperty('volume',1)
# print(type(voices))
    
def speak(text):
    """
    This function takes text and returns vioce
    args:
    text : string
    """
    engine.say(text)
    engine.runAndWait()
    

# Speech Recognition function
def takecommand():
    """_summary_
    
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source=source)
        
        try:
            print('Recognizing....')
            quary = recognizer.recognize_google(audio_data=audio,language='en-IN')
            print(f"User said: {quary}")
            
        except Exception as e:
            print('Say that again please...')
            return 'None'
        return quary
    
text = takecommand()
speak(text=text)
            