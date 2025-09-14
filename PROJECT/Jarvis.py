from Brain.Aibrain import ReplyBrain
from Body.Speak import Speak
from Body.Listen import MicExecution
from Features.Wakeup import Listen
from Main import MainTaskExecution
print("Starting the Zeus : ")

def MainExecution():
    Speak("Hello Sir")


    while True:
        Data = MicExecution().lower()
        Data = str(Data)
        ValueReturn = MainTaskExecution(Data)
        if ValueReturn== True:
            pass
        
        Reply = ReplyBrain(Data)
        Speak(Reply)

    
def Wakk():
    query = Listen()
    if "wake up" in query:
        MainExecution()
    else:
        pass
    

Wakk()