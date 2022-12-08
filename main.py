import pyttsx3
import speech_recognition as sr
import datetime
import feature
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[8].id)
engine.setProperty('rate',170)

def speak(audio):
        print(" ")
        print('Gideon:' + audio)
        engine.say(audio)
        engine.runAndWait()

def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 1
        command.energy_threshold = 300
        audio = command.listen(source,0,5)

        try:
                print("Recongizing.....")
                query = command.recognize_google(audio, language = 'en-in')
                print(f'You Said : {query}\n')

        except Exception as e:
                print('Say that again!')
                return "none" 
        return query.lower()

def greetMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,sir")
    elif hour >12 and hour<=18:
        speak("Good Afternoon ,sir")

    else:
        speak("Good Evening,sir")

    speak("Please tell me, How can I help you ?")


if __name__ == "__main__":
    while True:
        query = take_command().lower()
        if "wake up" in query:
            greetMe()

            while True:
                query = take_command().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 

                if 'hello' in query:
                        speak("Hello Sir, How are you?")

                elif "i am fine" in query:
                        speak("That's great, Sir")

                elif "how are you" in query:
                        speak("My Ram need some cleaning, otherwise Perfect")

                elif 'thank you' in query:
                        speak("you are welcome, sir")
               
                elif 'who created you' in query:
                        speak("I was created by Mayank Atul Ghai")
                        speak('On 3rd Decemeber 2022')

                elif 'youtube search' in query:
                        speak ('Ok Sir, This is what I found!')
                        query = query.replace('Gideon', '')
                        query = query.replace('youtube search', '')
                        feature.yt_search(query)
                        

                elif 'youtube play' in query:
                        speak ('Ok Sir, This is what I found!')
                        query = query.replace('Gideon', '')
                        query = query.replace('youtube play', '')
                        feature.yt_play(query)
                        

                elif 'google' in query:
                        speak ('Ok Sir, This is what I found!')
                        query = query.replace('Gideon', '')
                        query = query.replace('Google search', '')
                        feature.Google_search(query)
                        

                elif 'wikipedia' in query:
                        speak('Searching for Wikipedia')
                        query = query.replace('Gideon', '')
                        query = query.replace('wikipedia', '')
                        feature.searchWikipedia(query)
                        
                elif 'set alarm' in query:
                        speak(f'Ok Sir, Setting the alarm')
                        query = query.replace('Gideon', '')
                        query = query.replace('', '')
                        feature.Alarm_time(query)

                elif "temperature" in query:
                        search = query.replace('Gideon', '')
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        temp = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {temp}")

                elif "weather" in query:
                        search = query.replace('Gideon', '')
                        url = f"https://www.google.com/search?q={search}"
                        r  = requests.get(url)
                        data = BeautifulSoup(r.text,"html.parser")
                        weather = data.find("div", class_ = "BNeawe").text
                        speak(f"current{search} is {weather}")

                elif "time" in query:
                        strTime = datetime.datetime.now().strftime("%H:%M")    
                        speak(f"Sir, the time is {strTime}")

                elif "goodbye" in query:
                        speak("Going to sleep,sir")
                        exit()
