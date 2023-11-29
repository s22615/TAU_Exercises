from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def PercentCalcTest():
    n1 = 5
    n2 = 3

    driver = webdriver.Chrome()

    driver.get("https://kalkulatorprocentow.pl")
    time.sleep(3)
    driver.find_element(By.ID, "percent").send_keys(n1)
    time.sleep(1)
    driver.find_element(By.ID, "percentValue").send_keys(n2)
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="p1"]/div[1]/div[5]/button[1]').click()
    time.sleep(3)

    res = driver.find_element(By.ID, 'percentResult')
    predicted_res = '0.15'

    if res.text == predicted_res:
        print("Correct result")
    else:
        print(f"Incorrect result. Should be: {predicted_res}")

    time.sleep(3)
    driver.close()


PercentCalcTest()

