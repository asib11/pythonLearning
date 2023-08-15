from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import datetime
from datetime import datetime

driver = webdriver.Chrome()
driver.maximize_window()

da=[]
data = pd.read_excel('data1.xlsx')

    # Iterate over the rows in the Excel sheet
for index, row in data.iterrows():
    
    m = row['maker']
    ya = row['firstRegister']
    mod = row['model']
    fueltype = row['Fueltype']
    geabox = row['Geabox']
    
    minimumBid=row['minimumBid']
    reserveBid=row['reserveBid']
    tittle=row['tittle']
    maker=row['maker']
    model=row['model']
    firstRegister=row['firstRegister']
    Fueltype=row['Fueltype']
    Horsepower=row['Horsepower']
    Geabox=row['Geabox']
    Odometer=row['Odometer']
    carauto1_url=row['carauto1_url'] 
    
    
    #maker
    driver.get('https://eng.auto24.ee/kasutatud/kasutatud.php')
    time.sleep(2)
    try:driver.find_element(By.XPATH,'//div[@class="banner-actions-container"]/button').click()
    except:print('year')
    try:
        driver.find_element(By.XPATH,'//*[@id="item-searchParam-cmm-1-make"]/div/div/div[1]/span[3]').click()
        time.sleep(2)
    except:
        continue
    try:
        maker = driver.find_element(by=By.XPATH, value="""//*[@id="item-searchParam-cmm-1-make"]/div/div/div[1]/span[2]""")
        maker.send_keys(m)
        time.sleep(2)
    except:
        prices("makter not send some issue there")
    #year
    try:
        driver.find_element(by= By.XPATH, value= '//*[@id="searchParam-year"]').click()
    except:
        continue
    try:
        year = driver.find_element(by= By.XPATH, value= '//*[@id="searchParam-year"]')
        y= ya.year
        
    except:
        try:
            ya_datetime = datetime.strptime(ya, '%m/%Y')  # Convert the string to a datetime object
            y = ya_datetime.year
        except:
            print(f"year not send issue,{y} ")
    try:
        year.send_keys(y)
        time.sleep(2)
    except:
        continue
    #model
    try:
        driver.find_element(By.XPATH,'//*[@id="item-searchParam-cmm-1-model_id"]/div/div/div[1]/span[3]').click()
        time.sleep(1)
        model = driver.find_element(by=By.XPATH, value="""//*[@id="item-searchParam-cmm-1-model_id"]/div/div/div[1]/span[2]""")
        model.send_keys(mod)
        driver.implicitly_wait(3)
    except:
        print("model not send ")
    #gare
    try:
        driver.find_element(By.XPATH,'//*[@id="item-searchParam-transmission"]/div/div/div[1]/span[3]').click()
        time.sleep(2)
        gare = driver.find_element(By.XPATH,'//*[@id="item-searchParam-transmission"]/div/div/div[1]/span[2]')
        gare.send_keys(geabox)
        time.sleep(1)
        driver.find_element(By.XPATH,'//*[@id="item-searchParam-transmission"]/div/div/div[2]/div[2]').click()
        time.sleep(2)
    except:
        print("gare box not select ")
    #fule
    try:
        driver.find_element(By.XPATH,'//*[@id="item-searchParam-fuel"]/div/div/div[1]/span[3]').click()
        time.sleep(2)
        fule = driver.find_element(By.XPATH,'//*[@id="item-searchParam-fuel"]/div/div/div[1]/span[2]')
        fule.send_keys(fueltype)
        time.sleep(2)
    except:
        print("Fule not selected ")
    
    driver.find_element(By.XPATH,'//input[@class="input-submit btn btn-success btn-l"]').click()
    time.sleep(2)
    #scraping data
    try:
        name = driver.find_element(By.XPATH,'(//div[@class="title"]/a)[1]').text
    except:
        name=''
    try:
        link = driver.find_element(By.XPATH,'(//div[@class="title"]/a)[1]').get_attribute('href')
    except:
        link=''
    try:
        prices = driver.find_element(By.XPATH,'(//span[@class="price"])[2]').text
    except:
        prices=''
    try:
        Url =driver.current_url
    except:
        Url=''
    
    da.append({'minimumBid':minimumBid,'reserveBid':reserveBid,'tittle':tittle,'maker':m,'model':mod,'firstRegister':firstRegister,'Fueltype':Fueltype,'Horsepower':Horsepower,'Geabox':Geabox,'Odometer':Odometer,'carauto1_url':carauto1_url , 'name':name,'Car_link':link,'prices':prices,'Page Url':Url
        
    })
   
    
df=pd.DataFrame(da)
df.to_excel(f'auto24 data3.xlsx',index=False)