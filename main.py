import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') 

        # sapi5 --> to use inbuilt voice of window  

voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.paused_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jonsnowgot2001@gmail.com','publicgmail')
    server.sendmail('jonsnowgot2001@gmail.com',to,content)
    server.close()
    
if __name__ == "__main__":
    #speak("shubham is a good boy")
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('searching...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Shubham\\OneDrive\\Desktop\\python project\\fav'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Shubham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shubham' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "myshubham2001@gmail.com"
                sendEmail(to, content)
                speak("done sir,Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry, some technical issue")

        elif 'quit' in query:
            exit()

