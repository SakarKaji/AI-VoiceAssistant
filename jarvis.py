import pyttsx3
import speech_recognition as sr #we use speechrecognition many times and it ll be long so we created shortcut as sr 

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
            command = listener.recognize_google_cloud(voice)
            command = command.lower()
            print(command)
            return command
    except:
        return ""

def run_jarvis():
    command = take_command()
    if 'hello' in command:
        talk('hi boss how are you')
    elif 'exit' in command:
        talk('goodbye!')
        exit()
    else:
        talk("i dont understand")

talk('hello world, mero naam jarvi')

while True:
    run_jarvis()



 