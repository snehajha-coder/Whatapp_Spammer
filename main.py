import  time
#from datetime import date, datetime

#import pyautogui
from selenium import webdriver
#import pyautogui
#from selenium.common.exceptions import NoSuchElementException
#from keyboard import press
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\Hp\AppData\Local\Google\Chrome\User Data\Default')
options.add_argument('--profile-directory=Default')

chrome_browser = webdriver.Chrome(executable_path=r'D:/softwares/edge web driver/chromedriver.exe', options=options)
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(20)

user_name_list = ['AMBUJ -1 Chem', 'Kshitij Chem -1']
msg = '🙂'


for user_name in user_name_list:

    user = chrome_browser.find_element_by_xpath('//span[@title ="{}"]'.format(user_name))
    user.click()
    #enter_key = chrome_browser.find_element_by_xpath('//button[@class="_4sWnG"]')

    time.sleep(20)
    message_box = chrome_browser.find_element_by_xpath('//div[@class="p3_M1"]')

    for i in range(30000):
        message_box.send_keys(msg + Keys.ENTER)
        print(i)

        #pyautogui.press('enter')
        #enter_key = chrome_browser.find_element_by_xpath('//button[@class="_4sWnG"]')
        #enter_key.click()

