import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime

from tomlkit import date

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#to convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak('say that again please...')
        return 'none'
    return query

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak('good morning')
    elif hour>12 and hour<18:
        speak('good afternoon')
    else:
        speak('good evening')
    speak("I'm jarvis sir. Please tell me, What can i help u ?")


if __name__=='__main__':
    # takecommand()
    # wish()
    # speak('hello sir how can i help u')
    while True:
        query = takecommand().lower()

        # logic building for tasks

        if 'open notepad' in query:
            path = 'C:\Windows\system32'