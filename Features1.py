import geocoder
import pywhatkit
import speech_recognition as sr
import webbrowser as web
import pyttsx3
import os
import subprocess
import pyautogui
import psutil
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()
    

def GoogleSearch(term):
    result = "https://www.google.com/search?gs_ssp=eJzj4tTP1TewzEouK1ZgNGB0YPBir8wvLSlNSgUAUQAG7g&q="+term
    web.open(result)
    Speak("This Is What I Found For Your Search .")

def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")

def open_google_calendar():
        calendar_url = "https://calendar.google.com"
        web.open(calendar_url)
        Speak("Opening Google Calendar. Have a look at your schedule.")

def SpeedTest():
    os.startfile("https://www.speedtest.net/")
    Speak("You Can Run And Check It Out.")

def note_pad():
    Speak("opening notepad.")
    os.system('notepad.exe')

def wp():
    Speak("opening whatsapp")
    web.open('https://web.whatsapp.com/')

def file_manager():
    Speak("opening file manager.")
    os.startfile("explorer.exe")

def calculator():
    Speak("Opening calculator...")
    os.startfile("https://mathsolver.microsoft.com/")
def spoti_fy():
    Speak("opening spotify.")
    subprocess.Popen(['spotify'])

def close():
    pyautogui.hotkey('alt', 'f4')

def run():
    Speak("opening excel.")
    os.startfile("excel.exe")

def mail():
    Speak("opening mail.")
    os.startfile("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

def news():
    Speak("see the latest news updates...")
    os.startfile("https://timesofindia.indiatimes.com/")

def translateLanguage():
    Speak("translate ....")
    os.startfile("https://translate.google.com/")

def vscode():
    Speak("opening vscode.")
    os.system("code")

def note():
    Speak("ok.")

def bat():
    battery = psutil.sensors_battery()
    if battery is None:
      print("Battery not found")
    else:
    # Get the battery percentage
      percent = battery.percent
      print("Battery percentage:", percent)

def My_Location():
    Speak("Checking your current location...")

    # Get user's current location using geocoder
    g = geocoder.ip('me')
    city = g.city
    country = g.country

    if city and country:
        Speak(f"Sir, you are currently in {city}, {country}.")
    else:
        Speak("Sorry, unable to determine your current location.")

    # Open Google Maps with the detected location
    if g.latlng:
        latitude, longitude = g.latlng
        url = f"https://maps.google.com/?q={latitude},{longitude}"
        web.open(url)

def comedy():
    Speak("have a look on this video...")
    os.startfile("https://www.youtube.com/watch?v=Vq1aXqbqrBw")

def word():
    Speak("opening Microsoft word")
    os.system('start winword')

def restart():
   Speak("Restarting System")
   os.system("shutdown /r /t 1")


def shutdownn():
    Speak("Shutdown system")
    os.system("shutdown /s /t 1")