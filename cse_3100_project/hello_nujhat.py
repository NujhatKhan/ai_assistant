import pyttsx3              #text-to-speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine=pyttsx3.init('sapi5')       #object creation, sapi5 is a microsoft text to speech engine
voices=engine.getProperty('voices')  #getting details of current voice
engine.setProperty('voice', voices[1].id)  # voice id 1 indicates female voice, 0 is for male voice

def speak(audio):            #converts text to speech
    engine.say(audio)
    engine.runAndWait()

def wishme():            #to greet the user
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
        print("Good Afternoon")
    else:
        speak("good evening")
        print("Good Evening")

    speak("I am a virtual assistant. How may i help you")

def takecommand():           #it takes microphone input from the user and returns string output
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Say something...")
        statement= r.recognize_google(audio,language='en-in')
        print(f"user said:{statement}\n")

    except Exception as e:
        print("Say that again...")
        return "None"
    return statement

if __name__=="__main__":
    speak("hello")
    wishme()
    if 1:
        statement=takecommand().lower()   #given command is stored in statement

        if 'wikipedia' in statement:
            speak("searching wikipedia...")
            statement=statement.replace("wikipedia"," ")
            result=wikipedia.summary(statement,sentences=2)
            speak("according to wikipedia..")
            print(result)
            speak(result)

        elif 'youtube' in statement:
            webbrowser.open_new_tab("youtube.com")
            speak("youtube is open now")

        elif 'google' in statement:
            webbrowser.open_new_tab("google.com")
            speak("google is open now")

        elif 'gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("gmail is open now")

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://www.prothomalo.com/")
            speak("newspaper is open now, happy reading")

        elif 'search' in statement:
            statement=statement.replace("search", " ")
            webbrowser.open_new_tab(statement)

        elif 'weather' in statement:
            webbrowser.open_new_tab("https://www.accuweather.com/en/bd/dhaka/28143/weather-forecast/28143")