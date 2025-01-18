from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
from config import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstaFollower:
    def __init__(self):
        chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
       self.driver.get('https://www.instagram.com/accounts/login/')
       WebDriverWait(self.driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys(USERNAME)
       WebDriverWait(self.driver, 20).until(
         EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys(PASSWORD)
       WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]'))
        ).click()

       time.sleep(10)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/vindiesel/')
        following = WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_7e"]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[3]/ul/li[2]/div/a'))
        )
        following.click()
        time.sleep(20)
        scroller = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroller)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
