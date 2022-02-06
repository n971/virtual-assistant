from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

Listener = sr.Recognizer()
engine= pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.runAndWait

def talk(text):
    engine.say(text)
    engine.runAndWait()
   
def take_command():  
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = Listener.listen(source)
            command= Listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command= command.replace('jarvis','')
            print(command)

    except:
        pass
    return command

def run_jarvis():
    command= take_command()
    print(command)
    if 'play' in command:
        song= command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        talk('the current time is'+time)
        print(time)
        
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
        
    elif 'activate' in command:
        talk('HEllO JAKE IM JARVIS YOUR VIRTUAL ASSISTANT,WEATHER IS GOOD TELL ME HOW CAN I HELP YOU ?')
    
    elif 'hello' in command:
        talk('hey im jarvis and i want love')   
    elif 'who made you' in command:
        talk('im created by sir jake')
    elif 'bye' in command:
        talk('see you again')
        quit
    else:
        talk('please say that command again')
        
while True:      
    run_jarvis()