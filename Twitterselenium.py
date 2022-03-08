import time, os, random
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class Twittergbot():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.gbot = webdriver.Chrome(
            options = chrome_options
        )
        
    def dummy_send(self, driver, element, word):    
        for c in word:
            delay = random.uniform(0.3, 2)
            driver.find_element_by_xpath(element).send_keys(c)
            time.sleep(delay)

    def login(self):
        bot = self.gbot
        bot.get('https://twitter.com/')
        time.sleep(random.uniform(0.5, 5))
        try:
            loginbtn = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div').click()
            time.sleep(random.uniform(0.5, 2))
            loginbtn.click()
        except:
            bot.close()
            self.__init__(self.username, self.password, self.email)
            bot = self.gbot
            bot.get('https://twitter.com/')
            time.sleep(random.uniform(0.5, 5))
            loginbtn = bot.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
            time.sleep(random.uniform(0.5, 2))
            loginbtn.click()
        
        time.sleep(random.uniform(4, 8))
        email = bot.find_element_by_xpath( '//*[@name="text"]')
        self.dummy_send(bot, '//input[@name="text"]', self.email)
        time.sleep(random.uniform(0.5, 5))
        email.send_keys(Keys.RETURN)
        time.sleep(random.uniform(0.5, 5))
        try:
            password = bot.find_element_by_xpath('//input[@name="password"]')
        except : 
            username = bot.find_element_by_xpath( '//*[@name="text"]')
            self.dummy_send(bot, '//input[@name="text"]', self.username)
            username.send_keys(Keys.RETURN)
        
        time.sleep(random.uniform(0.5, 5))
        password = bot.find_element_by_xpath('//input[@name="password"]')
        self.dummy_send(bot, '//input[@name="password"]', self.password)
        time.sleep(random.uniform(0.5, 5))
        password.send_keys(Keys.RETURN)
        time.sleep(random.uniform(0.5, 5))
        for i in bot.find_elements(By.XPATH, '//input'):
            print(i.get_attribute(name="name"))
            
    def browse(self):
        body = self.gbot.find_element_by_tag_name("body")
        body.send_keys(Keys.PAGE_DOWN);

if __name__=="__main__":
    chromedriver_autoinstaller.install()
    username = ""
    password = ""
    email = ""
    t=Twittergbot(username,password,email)
    t.login()
    time.sleep(random.uniform(0.5, 5))
    t.browse()
