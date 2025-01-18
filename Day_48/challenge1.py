from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_title = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {i: {"time": event_title[i].text, "name": event_name[i].text} for i in range(len(event_title))}

print(events)
