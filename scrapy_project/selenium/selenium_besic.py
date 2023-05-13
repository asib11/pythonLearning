# import csv
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# # from selenium.webdriver.chrome.options import Options
# # chrome_options = Options()
# #chrome_options.add_argument("--headless")

# with open('cases.csv','r') as file:
#     csv_reader = csv.reader(file)
#     for data in csv_reader:
#         driver = webdriver.Chrome()
#         driver.get("https://casesearch.courts.state.md.us/casesearch/inquiry-index.jsp")
#         time.sleep(5.0)
#         v1 = driver.find_element(by=By.XPATH, value="(//input[@name='disclaimer'])[1]")
#         time.sleep(1)
#         v1.click()
#         v2 = driver.find_element(by=By.XPATH, value="(//input[@id='btnDisclaimerAgree'])[1]")
#         time.sleep(0.3)
#         v2.click()
#         time.sleep(0.5)
#         v3 = driver.find_element(by=By.XPATH, value="(//input[@name='courttype'])[2]")
#         time.sleep(1.0)
#         v3.click()
#         time.sleep(0.5)
#         text_box = driver.find_element(by=By.XPATH,value= "(//input[@name='caseId'])[1]")
#         btn = driver.find_element(by=By.XPATH, value="(//input[@name='searchAppellCaseNumAction'])[1]")
#         text_box.send_keys(data)
#         time.sleep(5.0)
#         btn.click()
#         time.sleep(5)
#         print(driver.page_source)

# driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://eng.auto24.ee/kasutatud/kasutatud.php")
time.sleep(5)
driver.find_element(by=By.XPATH, value="//[@id='onetrust-accept-btn-handler']").click()
time.sleep(2)
#model = driver.find_element(by=By.XPATH, value='//div[@id="item-searchParam-cmm-1-model_id"]/div/div/div[1]/span[2]')
model = driver.find_element(by=By.XPATH, value='//input[@id="searchParam-year"]')
time.sleep(1)
model.click()
time.sleep(50)
#model.send_keys('Volkswagen Jetta 1.9 TDI Comfortline')
model.send_keys('2009')
time.sleep(2)

button = driver.find_element(by=By.XPATH, value="(//input[@name='otsi'])[1]")
button.click()