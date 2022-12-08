import pywhatkit
import wikipedia
from pywikihow import WikiHow, search_wikihow
import os
import pyttsx3
import webbrowser as web
from playsound import playsound
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[8].id)
engine.setProperty('rate',150)

def speak(audio):
        print(" ")
        print('Gideon:' + audio)
        engine.say(audio)
        engine.runAndWait()



def Google_search(term):
    # main.speak ('Ok Sir, This is what I found!')
    query = term.replace('gideon', '')
    query = query.replace('what is ', '')
    query = query.replace('how to ', '')
    query = query.replace('what do you mean by ', '')
    writeab = str(query)

    o = open("D:\Project\Gideon\Database\Google_Search_database.txt\n",'a')
    o.write(writeab)
    o.close()

    try:
            Query = str(term)
            pywhatkit.search(Query)

            if 'how to' in Query:
                max_result = 1
                how_to_func = search_wikihow(query = Query, max_results = max_result)
                assert len(how_to_func) == 1
                how_to_func[0].print()
                speak(how_to_func[0].summary)

            else:
                search = wikipedia.summary(Query,1)
                speak(f'According To Your Search : {search}')

    except:
        speak('No speakable output available')

def yt_search(term):
        result = 'https://www.youtube.com/results?search_query=' + term
        web.open(result)
        speak('Done, sir')
 
def yt_play(term):
    result = 'https://www.youtube.com/results?search_query=' + term
    pywhatkit.playonyt(term)
    speak('Done, sir')

def searchWikipedia(query):
        results = wikipedia.summary(query, sentences = 2 )
        speak('According to wikipedia ')
        print(results)
        speak(results)

      
# def Alarm_time(query):
#     Time_here = open("D:/Project/Gideon/Data.txt", 'a')
#     Time_here.write(query) 
#     Time_here.close()  
#     os.startfile('D:/Project/Gideon/Database/ExtraProg/Alarm.py')

# Alarm_time('set alarm for 7 hours and 27 minutes')