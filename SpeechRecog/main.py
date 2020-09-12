import pyttsx3
import speech_recognition as sr
from wolframAlphaFunction import *
from weatherFunction import *
from googleTranslateFunction import *
from wikipediaFunction import *
from todoListFunction import *
#import weatherFunction as wf

def process(text):
    text = text.lower()
    if ("my to do list" in text):
        return DAVIDtoDoList(text)
    elif ("homework" in text) or ("code" in text) or ("112" in text):
        return (f"Sorry, I cannot do that. That would be an academic integrity violation. " + 
                f"Please ask the TAs for help. If you go any further down this path "
                f"I will have to get the real David Kosbie")
    elif ("language" in text) or ("translate" in text):
        translate = Translate()
        return translate.DAVIDtranslator(text)
    elif ("weather" in text) or ("temperature" in text) or ("wind speed" in text) or ("humidity" in text):
        wf = WeatherAnswers()
        return wf.DAVIDweather(text)
    elif ("tell me about" in text) or ("talk about" in text):
        return getDAVIDFacts(text)
    else:
        return DAVIDwolframalpha(text)

def audioOutput(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    return


r = sr.Recognizer()
File = open("speechfile.txt","w+")
on = True
while on:
    with sr.Microphone() as source:
        # use the default microphone as the audio source
        # listen for the first phrase and extract it into audio data
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.record(source,duration=5)
        print("Running")
    try:
        audioInput = r.recognize_google(audio)
        #File.write(audioInput)    
        #File.close()
        print(audioInput)
        result = process(audioInput)
        print(result)
        audioOutput(result)
        break
        # recognize speech using Google Speech Recognition
    except sr.UnknownValueError:                            
    #    # speech is unintelligible
        print("Could not understand audio")



