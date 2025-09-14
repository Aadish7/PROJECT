import speech_recognition as sr



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
    print(query)
    return query


def WakeupDetected():
    queery = Listen().lower()

    if "wake up" in queery:
        print("Started")
    else:
        pass


