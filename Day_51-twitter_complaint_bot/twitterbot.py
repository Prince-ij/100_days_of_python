from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import *


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)


    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        return (float(self.up), float(self.down))


    def tweet_at_provider(self, msg):
        self.driver.get('https://x.com/i/flow/login')
        time.sleep(5)
        email = self.driver.find_element(By.NAME, 'text')
        email.send_keys(EMAIL)

        time.sleep(5)
        username = self.driver.find_element(By.NAME, 'text')
        username.send_keys('Babygirl_opp')

        time.sleep(5)
        passwd = self.driver.find_element(By.NAME, 'password')
        passwd.send_keys(PASSWORD)

        time.sleep(15)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(msg)
        time.sleep(5)
        tweet_send = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        tweet_send.click()
        time.sleep(30)
