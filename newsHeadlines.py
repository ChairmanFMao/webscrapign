from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import ctypes
import time

# This program goes to the frontpage of bbc news and takes a screenshot then sets it as
# the wallpaper on the device

# Starts up firefox and gets onto bbc website
driver = webdriver.Firefox(service_log_path="C:\\Users\\Freddie\\AppData\\Local\\Temp\\geckodriver.log")
driver.implicitly_wait(0.5)
driver.get("https://www.bbc.co.uk/")
# Removes the accept cookies message
driver.find_element(by=By.CLASS_NAME, value="exhqgzu2").click()
driver.find_element(by=By.CLASS_NAME, value="eki2hvo12").click()
# Maxmises the window - took so long to find lol
driver.fullscreen_window();
time.sleep(0.75)
# Takes a screenshot of the window
frontPage = pyautogui.screenshot()
    frontPage.save("C:/Users/Freddie/Documents/programming/webscraping/headlines.png")
# Sets the screenshot as the wallpaper for the sytem
ctypes.windll.user32.SystemParametersInfoW(20,0,"C:/Users/Freddie/Documents/programming/webscraping/headlines.png",0)

driver.close()