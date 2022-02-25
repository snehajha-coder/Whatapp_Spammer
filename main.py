import  time    
from selenium import webdriver   #used selenium to automate my chrome browser
from selenium.webdriver.common.keys import Keys        #imported keyboards


options = webdriver.ChromeOptions()            
options.add_argument(r'--user-data-dir=C:\Users\Hp\AppData\Local\Google\Chrome\User Data\Default')     #path where user recent data is stored so that you don't need to spam again and again
options.add_argument('--profile-directory=Default')

chrome_browser = webdriver.Chrome(executable_path=r'D:/softwares/edge web driver/chromedriver.exe', options=options)  #will open webdriver
chrome_browser.get('https://web.whatsapp.com/')  #will go to WhatApp web

time.sleep(20)  # will wait for 20s helpfull if internet speed is slow and to reduce errors which will cause due to hurry

user_name_list = ['AMBUJ -1 Chem', 'Kshitij Chem -1'] #list of peoples you want to disturb name exactly same as you saved in WhatApp
msg = '🙂' #the msg you want to send repetatively


for user_name in user_name_list:  #will go to each friend one by one

    user = chrome_browser.find_element_by_xpath('//span[@title ="{}"]'.format(user_name))   #will find the person
    user.click()
    time.sleep(20)
    message_box = chrome_browser.find_element_by_xpath('//div[@class="p3_M1"]')        # will find the msg box

    for i in range(3000):   #will send that msg 3000 times to each of them
        message_box.send_keys(msg + Keys.ENTER)           #will type and send msg
        print(i)
