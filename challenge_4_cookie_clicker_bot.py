from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# make it so that chrome does NOT automatically closes once youre done testing

chromedriver_path=Service("/chrome_driver/chromedriver.exe") 
driver = webdriver.Chrome(service=chromedriver_path, options=options)
# chromedriver with options
click = True
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_clicker = driver.find_element(By.ID, "cookie")
    
timeout = time.time() + 60*10 # 5 minutes from now stop loop
check_buy = time.time() + 5 # 5 seconds after check if theres anything u can buy

while True:

    time.sleep(0.0125)

    if time.time() > timeout:
        break

    else:

        cookie_clicker.click()

        # get the store item prices
        upgrade_prices = []
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")

        for price in prices:

            # print(price.text)
            try:
                pricez = price.text.split("-")[1].strip().replace(",","")
                upgrade_prices.append(int(pricez))

            except IndexError:
                pass

        money = driver.find_element(By.ID, "money")
        money_as_int = int(money.text)

        if time.time() > check_buy:
        
            if money_as_int >= upgrade_prices[7]:
                buyTimeMachine = driver.find_element(By.ID, " buyElder pledge")
                buyTimeMachine.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[6]:
                buyPortal = driver.find_element(By.ID, "buyPortal")
                buyPortal.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[5]:
                buyAlchemy = driver.find_element(By.ID, "buyAlchemy lab")
                buyAlchemy.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[4]:
                buyShipment = driver.find_element(By.ID, "buyShipment")
                buyShipment.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[3]:
                buyMine = driver.find_element(By.ID, "buyMine")
                buyMine.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[2]:
                buyFactory = driver.find_element(By.ID, "buyFactory")
                buyFactory.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[1]:
                buyGrandma = driver.find_element(By.ID, "buyGrandma")
                buyGrandma.click()
                cookie_clicker.click()
            
            elif money_as_int >= upgrade_prices[0]:
                buyCursor = driver.find_element(By.ID, "buyCursor")
                buyCursor.click()
                cookie_clicker.click()
            
            check_buy = time.time() + 5 # reset check_time by adding another 5 seconds to current time
        
        