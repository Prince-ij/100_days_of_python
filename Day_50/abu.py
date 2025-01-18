from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
class Portal:
    def __init__(self, user, password):
        chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.username = user
        self.password = password

    def print_examcard(self):
        self.driver.get('https://portal.abu.edu.ng/')
        self.driver.find_element(By.NAME, 'username').click()
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.TAG_NAME, 'button').click()

        self.driver.find_element(By.XPATH, '//*[@id="menusection"]/div/div/ul[2]/li[6]/a').click()
        self.driver.find_element(By.ID, 'print').click()
        time.sleep(30)
