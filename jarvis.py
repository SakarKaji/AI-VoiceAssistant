import pyttsx3
import speech_recognition as sr #we use speechrecognition many times and it ll be long so we created shortcut as sr 
import datetime
import pyjokes
import pyaudio

listener = sr.Recognizer() #listener is a variable and recognizer is a fn


engine = pyttsx3.init() #engine is variable and init is a function

voices = engine.getProperty('voices') # voices is also a variable 

engine.setProperty('voice',voices[1].id)

engine.setProperty('rate',150) #rate of speed is 200


# engine.say('hello world vandeeu') #makes jarvis speak
# engine.runAndWait()

def talk(text): #talk is a fn
    engine.say(text) 
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google_cloud(voice, language="en")
            command = command.lower()
            print(command)
            return command
    except:
        return ""
    
def greeting() :
    current_time = datetime.datetime.now()
    hour = current_time.hour
    print(current_time,hour)
    if 3 <= hour <= 12:
     talk('goodmornin sir')
    elif 12 <= hour <17:
     talk('goodafternoon sir')
    elif 17 <= hour <19:
     talk('goodevening sir')




# def run_jarvis():
#     command = take_command()
#     if 'hello' in command:
#         talk('hi boss how are you')
#     elif 'exit' in command:
#         talk('goodbye!')
#         exit()
#     else:
#       talk("i dont understand")
     
def run_jarvi():
     command = take_command()
    #  if 'hello' in command:
    #     talk('hi boss how are you')
     if 'joke' in command:
       talk(pyjokes.get_joke())

talk('hello world, mero naam jarvi')

greeting()

while True:
    run_jarvi()






 