from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service(executable_path="/driver_path")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

# Cookie consent handling
try:
    # Wait for the cookie consent element to appear
    cookie_consent = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "KxvlWc"))
    )
    
    # Find the close button and click on it
    close_button = cookie_consent.find_element(By.ID, "W0wltc")
    close_button.click()
    
    # Wait for the cookie consent element to disappear
    WebDriverWait(driver, 1).until_not(
        EC.presence_of_element_located((By.CLASS_NAME, "KxvlWc"))
    )
    
except Exception as e:
    print("Error handling cookie consent:", e)


#googleda search bar cikasaya kadar bekle
WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME , "gLFyf")))
#search bari bul
input_element = driver.find_element(By.CLASS_NAME , "gLFyf")
#search barina yaz ve enter tusuna bas
input_element.clear()
input_element.send_keys("burakmert824" + Keys.ENTER)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Burak")
#find_elements ile birden fazla elementi bulabiliriz

print(link.text)   # Burak Ersoz
link.click()


time.sleep(10)
