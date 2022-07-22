# This program goes onto python.org and gets the word in a donate box

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_elements(by=By.XPATH, value='//a[@class="donate-button"]')
print(elem[0].text)
driver.close()

# This is so epic
# test test tests