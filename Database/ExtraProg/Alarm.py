import os 
from playsound import playsound
import datetime

extracted_time = open("D:/Project/Gideon/Data.txt",'rt')
time = extracted_time.read()
Time = str(time)

delete_time = open("D:/Project/Gideon/Data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

def ringer_now(time):

    time_to_set = str(time)
    time_now = time_to_set.replace('Gideon',"")
    time_now = time_now.replace('set','')
    time_now = time_now.replace('alarm',"")
    time_now = time_now.replace('for',"")
    time_now = time_now.replace("hours","")
    time_now = time_now.replace('minutes',"")
    time_now = time_now.replace(' and ',':')
    time_now = time_now.replace('set alarm for ','')

    Alarm_time = str(time_now)
    Alarm_time = Alarm_time.strip()
    print(Alarm_time)
    AlarmH = Alarm_time[0:2]
    AlarmM = Alarm_time[-2:]

    while True :

    # current_time = datetime.datetime.now().strftime("%H:%M")

        if (int(AlarmH) == int(datetime.datetime.now().hour) and int(AlarmM) == int(datetime.datetime.now().minute)):
            playsound("D:/Project/Gideon/Database/Alarm Sound/iron_man.mp3")

        elif (int(AlarmH) < datetime.datetime.now().hour or int(AlarmM) < datetime.datetime.now().minute):
            break

ringer_now(Time)

