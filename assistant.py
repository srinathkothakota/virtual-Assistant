import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
listener =sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')

                print(command)
    except:
        pass
    return command
def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing song'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')#%H:%M
        print(time)
        talk('current time is'+time)
    elif 'who is ram' in command:
        person = command.replace('who is ram', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry ,i have a boy friend')
    elif 'do you love me' in command:
        talk('yes , i love u')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'call' in command:
        num=command.replace('call', '')
        print('ok calling....'+num)
    elif 'exit' in command or 'bye' in command or 'sleep' in command:
        talk('ok , bye')
        exit()
    else:
        talk('I can not understand, what you saying ')


while True:
    run_alexa()
