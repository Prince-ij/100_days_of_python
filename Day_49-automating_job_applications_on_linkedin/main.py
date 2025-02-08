from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from config import EMAIL, PASSWORD

chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=4042553734&f_AL=true&geoId=105365761&keywords=python%20intern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true')
time.sleep(5)
sign_in = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
sign_in.click()

time.sleep(2)
email = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_key"]')
email.send_keys(EMAIL)
passwd = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')
passwd.send_keys(PASSWORD)
submit = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
submit.click()
save_apply = driver.find_elements(By.CSS_SELECTOR, '.class="jobs-save-button artdeco-button artdeco-button--secondary artdeco-button--3"')
for apply in save_apply:
    apply.click()
time.sleep(10)
