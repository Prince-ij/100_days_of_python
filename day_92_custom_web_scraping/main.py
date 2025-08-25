# Scraping the NBA Player Stats

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

import tempfile
import time

service = Service("/usr/local/bin/chromedriver")
options = webdriver.ChromeOptions()

# GUI mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")
options.add_argument("--start-maximized")
# Do NOT add --headless

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.nba.com/stats/leaders?SeasonType=Playoffs")

data = []

rows = driver.find_elements(By.TAG_NAME, 'tr')
for row in rows[1:]:
    inner_rows = row.find_elements(By.TAG_NAME, 'td')[1:9]
    inner_data = []
    for info in inner_rows:
        inner_data.append(info.text)
    data.append(inner_data)



with open('nba_player_stats.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['player', 'team', 'gp', 'min', 'pts', 'ftm', 'fga', 'fg%'])
    for player in data:
        writer.writerow(player)

time.sleep(10)
driver.quit()
