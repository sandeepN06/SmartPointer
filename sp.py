from selenium import webdriver 
from time import sleep 
import chromedriver_autoinstaller
import speech_recognition as sr 
import pyttsx3 
import pyautogui



while(True):

    try:
        r = sr.Recognizer() 




        with sr.Microphone() as source2: 
                

            r.adjust_for_ambient_noise(source2, duration=0.2) 
                
                
            audio2 = r.listen(source2) 
                
                
            MyText = r.recognize_google(audio2) 
            MyText = str(MyText.lower())




        if MyText == "search":
            pyautogui.hotkey('ctrl', 'c')
            chrome_options = webdriver.ChromeOptions()
            capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
            capabilities.update(chrome_options.to_capabilities())

            chromedriver_autoinstaller.install()

            driver = webdriver.Chrome()
            driver.set_window_size(1920, 1080)
            driver.implicitly_wait(10)
            driver.get("https://www.google.com/") 
            driver.find_element_by_xpath("/html/body//form[@role='search']/div[2]/div[1]//div[@class='a4bIc']/input[@role='combobox']").send_keys(pyautogui.hotkey('ctrl', 'v'))

        elif MyText == "stop":
            break




    except Exception as e:

        pyautogui.press('enter')


        