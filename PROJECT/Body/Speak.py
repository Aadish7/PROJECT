from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep


chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = False
Path = "Database\chromedriver.exe"
s = Service(Path)
driver = webdriver.Chrome(service= s,options=chrome_options)
driver.maximize_window()
website = r"https://tts.5e7en.me/"
driver.get(website)

def Speak(Text):

    lengthoftext = len(str(Text))

    if lengthoftext==0:
        pass

    else:
        print("")
        print(f"AI : {Text}")
        print("")
        Data = str(Text)
        xpathofsec = '//*[@id="text"]'
        driver.find_element(By.XPATH,value=xpathofsec).send_keys(Data)
        driver.find_element(By.XPATH,value='//*[@id="button"]').click()
        driver.find_element(By.XPATH,value='//*[@id="text"]').clear()

        if lengthoftext>=30:
            sleep(4)

        elif lengthoftext>=40:
            sleep(6)
        
        elif lengthoftext>=60:
            sleep(8)

        elif lengthoftext>=70:
            sleep(10)

        elif lengthoftext>=100:
            sleep(12)

        elif lengthoftext>=120:
            sleep(15) 

        else:
            sleep(2)




