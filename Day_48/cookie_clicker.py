import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element(By.ID, 'cookie')

start_time = int(time.time())
end_time = start_time + (5 * 60)
max_upgrade = 0
while True:
    cookie.click()

    start_time = int(time.time())

    if start_time % 10 == 0:
        # go through list of upgrades
        upgrades = [upgrade for upgrade in driver.find_elements(By.CSS_SELECTOR, '#store div[onclick]')]
        upgrade_prices = []

        for price in driver.find_elements(By.CSS_SELECTOR, '#store b'):
            try:
                price = price.text.split('-')[1]
                upgrade_prices.append(price)
            except IndexError:
                pass


        prices = [int(price.replace(',', '')) for price in upgrade_prices]

        # find the maximum upgrade I can afford
        for upgrade in prices:
            money = int(driver.find_element(By.ID, 'money').text)
            if (upgrade >= max_upgrade) and (money > upgrade):
                max_upgrade = upgrade
        # click on it
        try:
            indices = prices.index(max_upgrade)
            current = upgrades[indices]
            current.click()
        except ValueError:
            pass




    if end_time <= start_time:
        cps = driver.find_element(By.ID, 'cps').text
        print(f"cps: {cps}\nMoney: {money}")
        break
