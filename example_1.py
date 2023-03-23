import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://www2.nipponsoft.co.jp/bldoko/index.asp')
time.sleep(3)  # Let the user actually see something!
driver.maximize_window()
search_box = driver.find_element(By.ID,'menu2').click()
time.sleep(3)

driver.find_elements(By.NAME,'seimei')[1].click()
time.sleep(3)

driver.find_element(By.NAME,'submit_ranking').click()
time.sleep(3)

with open('names.txt', 'w') as w:
    while True:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find_all('td', attrs={'class': None})
        names = [str(c.contents[0]) for c in soup.find_all('td', attrs={'class': None})]
        str_names = '\n'.join(names)
        print(str_names)
        w.write(str_names)
        w.flush()
        driver.find_elements(By.CLASS_NAME,'submit_button')[-1].click()
        time.sleep(3)

driver.quit()
