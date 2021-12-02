from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
 
driver = webdriver.Chrome("D://Selenium//chromedriver_win32//chromedriver.exe")  
 
driver.maximize_window()  

driver.delete_all_cookies()  

driver.get("https://www.amazon.in/")  

driver.find_element_by_id("twotabsearchtextbox").send_keys("bags")  
time.sleep(2)

driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(2)

#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/div[1]/div/div/span/a/div/img").click()
driver.get("https://www.amazon.in/Northzone-Polyester-School-Backpack-Compartment/dp/B08678P2T7/ref=sr_1_1_sspa?keywords=bags&qid=1637812536&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExRVczS0w2Qzg3Q1dIJmVuY3J5cHRlZElkPUEwMjE1OTYyM05aUlNPTjA3WTY3RyZlbmNyeXB0ZWRBZElkPUEwNTM5NDY2M0ZYMUxNVDZPNU1aTCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
time.sleep(1)  

driver.find_element_by_id("add-to-cart-button").click()
time.sleep(2)

driver.find_element_by_id("/html/body/div[1]/div[1]/header/div/div[1]/div[3]/div/a[4]/div[2]/span[2]").click()
time.sleep(2)

driver.find_element_by_id("proceed-to-checkout-action").click()
time.sleep(2)
driver.find_element_by_id("hlb-view-cart-announce").click()
time.sleep(2)
driver.close()  
print("successfully added to cart")