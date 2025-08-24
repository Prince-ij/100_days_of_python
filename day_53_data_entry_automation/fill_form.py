from config import rental_platform_url, HEADERS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from apartments import RentApartments

class FillForm:
    def __init__(self, url):
        chrome_driver_path = r"C:\Program Files\chromedriver-win32\chromedriver.exe"
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.url = url

        self.driver.get(self.url)

        zilo = RentApartments(rental_platform_url, HEADERS)
        links = zilo.get_links()
        addr = zilo.get_address()
        prices = zilo.get_prices()
        for i in range(len(prices)):
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addr[i])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[i])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(links[i])
            self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
            self.driver.get(self.url)
