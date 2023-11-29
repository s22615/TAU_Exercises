from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def RedditTest():
    username = "username"
    password = "password"

    driver = webdriver.Chrome()

    driver.get("https://www.reddit.com/login/")

    time.sleep(3)
    driver.find_element(By.ID, "loginUsername").send_keys(username)
    driver.find_element(By.ID, "loginPassword").send_keys(password)

    driver.find_element(By.XPATH, '//button[@class="AnimatedForm__submitButton m-full-width"]').click()

    time.sleep(3)
    error_message = "Incorrect username or password"

    error = driver.find_element(By.CLASS_NAME, "AnimatedForm__errorMessage")

    if error.text == error_message:
        print("Login failed")
    else:
        print("Login successful")

    time.sleep(3)
    driver.close()


RedditTest()
