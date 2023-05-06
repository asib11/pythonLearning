from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.wordhippo.com/")
time.sleep(5.0)
v1 = driver.find_element(by=By.XPATH, value="(//input[@id='anotherword'])[1]")
time.sleep(1)
v1.send_keys("community")
time.sleep(1)
v2 = driver.find_element(by=By.XPATH, value="(//input[@value='find it'])[1]")
v2.click()