 
from email.mime import audio
from gettext import install
from pickle import TRUE
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio 
import wikipedia
import os
import webbrowser
import smtplib


engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
 
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good moorning yusra")
    elif hour>=12 and hour <18:
        speak("good afternoon yusra")
    else:
        speak("good evening Yusra")
    speak("i am Sandra please tell me what can i do for you")
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)
        speak("could you please say that again")
        return"None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yusrafatimaaaaaaaa@gmail.com', 'dfzkwbsanneurlys')
    server.sendmail('yusrafatimaaaaaaaa@gmail.com', to, content)
    server.close()

if __name__=="__main__":
    wishme()    
    while True:
        query = takecommand().lower()
    
        if 'wikipedia' in query : 
            speak('searching wikipedia...')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'spotify' in query:
            webbrowser.open("spottify.com")
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open vs code' in query:
            codePath ="C:\\Users\\yusra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'PowerPoint' in query:
            powerCode="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(powerCode)
        elif 'canva' in query:
            canvaCode="C:\\Users\\yusra\\AppData\\Local\\Programs\\Canva\\Canva.exe"
            os.startfile(canvaCode)
        elif 'send email to yusra' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "yusraaafatimaap@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry somethimg went wrong")
        elif 'quit' in query:
            speak("ok bye yusra take care")
            quit()