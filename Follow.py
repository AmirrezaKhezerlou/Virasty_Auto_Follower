from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys        
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = webdriver.ChromeOptions()


def login(bot,url,phonenumber,password1,target):
    bot.get(url)
    wait = WebDriverWait(bot, 10)
    phone = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="tel-national"]')))
    phone.clear()
    phone.send_keys(phonenumber)
    time.sleep(2)
    checkMark = wait.until(EC.visibility_of_element_located((By.XPATH, '//span[@class="s-4 rounded-2px border-2 border-black ms-2 shrink-0"]')))
    webdriver.ActionChains(bot).move_to_element(checkMark).click(checkMark).perform()                    
    phone.send_keys(Keys.RETURN)
    time.sleep(5)
    password = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
    password.clear()
    password.send_keys(password1)
    password.send_keys(Keys.RETURN)
    time.sleep(5)
    startFollow(bot,target)



def startFollow(bot,target):
    bot.get('https://virasty.com/'+target+'/followers')
    while (True):
        try:
            wait = WebDriverWait(bot, 10)
            follow_Button = wait.until(EC.visibility_of_element_located((By.XPATH, '//button[@class="n-3ocqtz bg-black border-transparent n-1hhqp0"]')))
            webdriver.ActionChains(bot).move_to_element(follow_Button).click(follow_Button).perform() 
            time.sleep(1) 
        except:
           print('Except Coused Not Found any follow button yet')
           bot.execute_script('window.scrollBy(0,document.body.scrollHeight)')        
