from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)


file = pd.read_excel('data1.xlsx')
makers = file['maker'].tolist()
titles = file['tittle'].tolist()
year = file['firstRegister'].tolist()
hw = file['Horsepower'].tolist()
fuel = file['Fueltype'].tolist()
gear = file['Geabox'].tolist()

for maker in range(len(makers)):
    try:

        driver.get("https://eng.auto24.ee/kasutatud/kasutatud.php")
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value="""//*[@id="onetrust-accept-btn-handler"]""").click()
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value="""//*[@id="item-searchParam-cmm-1-make"]/div/div/div[1]""").click()
        driver.implicitly_wait(10)
        #driver.find_element(by=By.XPATH, value="""//*[@id="item-searchParam-cmm-1-make"]/div/div/div[1]/span[2]""").send_keys('Volkswagen')
        model = driver.find_element(by=By.XPATH, value="""//*[@id="item-searchParam-cmm-1-make"]/div/div/div[1]/span[2]""")
        model.send_keys(f'{makers[maker]}')
        time.sleep(5)
        #driver.find_element(by=By.XPATH, value="""//*[@id="item-searchParam-cmm-1-make"]/div/div/div[1]/span[2]""").send_keys(Keys.ENTER)
        model.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)

        title = driver.find_element(by=By.XPATH, value= '//*[@id="searchParam-cmm-1-model"]')
        title.send_keys(f'{titles[maker]}')
        time.sleep(5)
        title.click()
        time.sleep(5)
        #
        # #time.sleep(5)
        driver.find_element(by= By.XPATH, value= '//*[@id="searchParam-year"]').send_keys(f'{year[maker]}')
        time.sleep(5)
        driver.find_element(by= By.XPATH, value= '//*[@id="searchParam-year"]').click()
        #driver.implicitly_wait(10)
        time.sleep(5)
        #
        driver.find_element(by= By.XPATH, value= '//*[@id="searchParam-power_kw"]').send_keys(f'{hw[maker]}')
        time.sleep(5)
        driver.find_element(by= By.XPATH, value= '//*[@id="searchParam-power_kw"]').click()
        #driver.implicitly_wait(10)
        time.sleep(5)
        #
        driver.find_element(by=By.XPATH, value= '//*[@id="item-searchParam-fuel"]/div/div/div[1]/span[3]').click()
        time.sleep(2)
        driver.find_element(by=By.XPATH, value= '//*[@id="item-searchParam-fuel"]/div/div/div[1]/span[2]').send_keys(f'{fuel[maker]}')
        time.sleep(5)
        driver.find_element(by=By.XPATH, value= '//*[@id="item-searchParam-fuel"]/div/div/div[1]/span[2]').click()
        # #time.sleep(5)
        driver.implicitly_wait(10)
        driver.find_element(by=By.XPATH, value= '//*[@id="item-searchParam-transmission"]/div/div/div[1]/span[3]').click()
        time.sleep(2)
        driver.find_element(by= By.XPATH, value= '//*[@id="item-searchParam-transmission"]/div/div/div[1]/span[2]').send_keys(f'{gear[maker]}')
        time.sleep(5)
        driver.find_element(by= By.XPATH, value= '//*[@id="item-searchParam-transmission"]/div/div/div[1]/span[2]').send_keys(Keys.ENTER)
        time.sleep(5)





        button = driver.find_element(by=By.XPATH, value="""//*[@id="vehicleSearchForm-2"]/div/div/div[7]/div[1]/div/input""")
        driver.implicitly_wait(10)
        button.send_keys(Keys.ENTER)
        time.sleep(10)
    except:
        print('error')
driver.quit()