from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Max number of questions you can get is 70

# Opens a text file storing my login details
details = open("./userPassword.txt","r")

# Starts up firefox and logs me in
driver = webdriver.Firefox()
driver.get("https://www.drfrostmaths.com/timestables-game.php")
driver.implicitly_wait(5)
username = driver.find_element(by=By.NAME, value="login-email")
username.send_keys(details.readline())
password = driver.find_element(by=By.NAME, value="login-password")
secret = details.readline()
password.send_keys("".join([chr(ord(i)+13) for i in secret]))
password.send_keys(Keys.RETURN)
driver.implicitly_wait(0.5)

# Starts the times tables test
start = driver.find_element(by=By.XPATH, value='//a[@class="very-large-button-variant"]')
start.click()

# Gets and answers the questions
# Runs the code for 30 seconds
startingTime = time.time()
# while time.time() - startingTime < 30:
#     # Gets the question from the page
#     question = driver.find_element(by=By.ID, value="question")
#     # Replaces ÷ and × with their coding equivalent and evaluates the expression
#     answer = eval((question.text).replace(" ","").replace("÷","/").replace("×","*"))
#     # Inputs the answer in the box
#     answerBox = driver.find_element(by=By.ID, value="calculator-display")
#     answerBox.send_keys(str(int(answer)))

for i in range(70):
    # Gets the question from the page
    question = driver.find_element(by=By.ID, value="question")
    # Replaces ÷ and × with their coding equivalent and evaluates the expression
    answer = eval((question.text).replace(" ","").replace("÷","/").replace("×","*"))
    # Inputs the answer in the box
    answerBox = driver.find_element(by=By.ID, value="calculator-display")
    answerBox.send_keys(str(int(answer)))
    
answerBox = driver.find_element(by=By.ID, value="calculator-display")
answerBox.send_keys("gaming")

# This is commented out just so that the webpage doesn't close when the program finishes
# driver.close()