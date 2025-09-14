import speech_recognition as sr
from googletrans import Translator

#Listen To Voice Command In Hindi Or English
def Listen(): #create Function

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening>>>>>") #To know jarvis is listening
        r.pause_threshold = 1
        audio = r.listen(source,0,8) #This goes to listening mode
        

    try:
        print("Recognizing>>>")
        query = r.recognize_google(audio,language="en")
    except:
        return ""
    
    query = str(query).lower()
    return query


# Translation 

def TransHindiToEnglish(Text): #Defining function
    line = str(Text) #Converts text to string
    trans = Translator() #Calling / retriving Translator() class in this function which we imported above
    result = trans.translate(line) #using Translate function to translate line 
    data = result.text #retriving text from result
    print(data)
    return data

#Connect

def MicExecution():
    query = Listen()
    data =  TransHindiToEnglish(query)
    return data


