from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
second_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')

first_name.send_keys('Ibrahim')
second_name.send_keys('Muhammad')
email.send_keys('aishatu@gmail.com')

driver.find_element(By.TAG_NAME, 'button').click()
