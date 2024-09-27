from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/driverpath")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie_count_id = "cookies"
big_cookie_id = "bigCookie"

product_id_prefix = "product"
product_price_id_prefix = "productPrice"

# Cookie consent handling
time.sleep(4)
#it waits for the cookie consent element to appear and then clicks on it
# By.XPATH ile htmlde arama yapabiliriz ve contains() fonksiyonu ile bir elementin icindeki texti arayabiliriz
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Consent')]")))
driver.find_elements(By.XPATH, "//*[contains(text(), 'Consent')]")[1].click()

driver.find_element(By.ID, "langSelect-EN").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
big_cookie = driver.find_element(By.ID, big_cookie_id)
print("Cookie clicked")

while True:
    big_cookie.click()
    cookie_count = driver.find_element(By.ID, cookie_count_id).text.split(" ")[0]
    cookie_count = int(cookie_count.replace(",", ""))   # 1,000 -> 1000
    print(cookie_count)
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_id_prefix + str(i)).text.split(" ")[0]
        if not product_price.isdigit():
            continue
        product_price = int(product_price.replace(",",""))
        if(product_price <= cookie_count):
            product = driver.find_element(By.ID, product_id_prefix + str(i))
            product.click()
            break
        
        
    
    
time.sleep(200)
