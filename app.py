from src.helper import takecommand,speak,wish_me
import webbrowser,datetime,wikipedia,os


if __name__ == "__main__":
    wish_me()
    while True:
        query = takecommand().lower()
        # speak(text=query)
        
        if 'wikipedia' in query:
            speak('serching in wikipedia..')
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
            
        elif 'youtube' in query:
            speak('Opening youtube')
            webbrowser.open('youtube.com')
        
        elif 'google' in query:
            speak('Opening google')
            webbrowser.open('google.com')
            
        #This query for say the times
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")


        elif 'goodbye' or 'good bye' or 'bye-bye' in query:
            speak("ok sir. I am always here for you. bye bye")
            exit()