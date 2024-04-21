from Features1 import GoogleSearch, YouTubeSearch, SpeedTest, My_Location, wp, note_pad, file_manager, spoti_fy, word, open_google_calendar, close, news, translateLanguage, calculator, comedy, run, bat, mail, vscode, shutdownn, restart
from DataBase.ChatBot.ChatBot import ChatterBot
from JarvisUi import Ui_JarvisUi
import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    Ui_JarvisUi.display(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("Waiting ")
    Ui_JarvisUi.display("Waiting ")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")


Speak("Hello user")
Ui_JarvisUi.display("Hello user")


def TakeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        Speak("Listening")
        Ui_JarvisUi.display("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(": Recognizing...")
        Ui_JarvisUi.display(": Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f": Your Command : {query}\n")
        Ui_JarvisUi.display(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()


if __name__ == '__main__':
    wishMe()


def TaskExe():
    while True:
        query = TakeCommand()
        Ui_JarvisUi.display(query)

         #1. google
        if 'google search' in query:
            res =query[13:]
            GoogleSearch(res)

        #2. youtube
        elif 'youtube search' in query:
            url = "https://www.youtube.com"
            Query = query.replace("jarvis", "")
            url = Query.replace("youtube search", "")
            YouTubeSearch(url)

        #3. speed test
        elif 'speed test' in query:
            SpeedTest()     

        #4. location
        elif 'my location' in query:
            My_Location()

        #5. WP
        elif 'open whatsapp' in query:
            wp()

        #6. Notepad
        elif 'open notepad' in query:
            note_pad()

        #7. FM
        elif 'open file manager' in query:
            file_manager()

        #8. Spotify
        elif 'open spotify' in query:
            spoti_fy()

        #9. Word
        elif 'open microsoft word' in query:
            word()

        #10. GC
        elif 'open google calendar' in query:
            open_google_calendar()

        #11. Close current opened page
        elif 'close this' in query:

            close()

        #12. news
        elif 'check news updates' in query:
            from Features1 import news
            news()

        #13. LT
        elif 'translate language' in query:
            translateLanguage()

        #14. Calc
        elif 'open calculator' in query:
            calculator()

        #15. Joke
        elif 'comedy' in query:
            comedy()

        #16. Excel
        elif 'open excel' in query:
            run()

        #17. battery
        elif 'check battery' in query:
            bat()

        #18. GMAIL
        elif 'open email' in query:
            mail()

        #19. VS
        elif 'open vs code' in query:
            vscode()

        #20. shutdown
        elif 'shutdown' in query:
            shutdownn()

        #21. restart
        elif 'restart' in query:
            restart()
            
        else:
            reply = ChatterBot(query)
            Speak(reply)

            if 'bye' in query or 'exit' in query or 'go' in query:
                break

        Ui_JarvisUi.display(query)

if __name__ == '__main__':
    TaskExe()
