import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import playsound
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3 .init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M% %p')
        print(time)
        talk('current Time is ' + time )
    elif 'Who the he is' in command:
        person = command.replace('Who the he is', '')
        info = wikipedia.summary(person,1)
        talk(info)
    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        talk("Here you go to Google\n")
        webbrowser.open("google.com")
    elif 'open stackoverflow' in command:
        talk("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
while True:
    run_alexa()