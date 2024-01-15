import pyttsx3

engine = pyttsx3.init() #engine is variable and init is a function

voices = engine.getProperty('voices') # voices is also a variable 

engine.setProperty('voice',voices[1].id)

engine.setProperty('rate',150) #rate of speed is 200


# engine.say('hello world vandeeu') #makes jarvis speak
# engine.runAndWait()

def talk(text): #talk is a fn
    engine.say(text) 
    engine.runAndWait()
talk('hello world vandeeu')

 