import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ", "")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameoftheapp = Query.replace("open","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(0.5)
        keyboard.press('enter')
        return True
    
    elif "start" in Query:
        Nameoftheapp = Query.replace("open", "")
        if "chrome" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return True
        elif "brave" in Nameoftheapp:
            os.startfile(r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")
            return True
        elif "spotify" in Nameoftheapp:
            os.startfile(r"C:\Users\kalpe\AppData\Local\Microsoft\WindowsApps\Spotify.exe")
            return True
        elif "visual studios" and "vs code" in Nameoftheapp:
            os.startfile(r"C:\Users\kalpe\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            return True
        elif "android studios" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Android\Android Studio\bin\studio64.exe")
            return True
        elif "word" in Nameoftheapp:
            os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
            return True
