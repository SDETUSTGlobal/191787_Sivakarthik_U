from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("D://Selenium//chromedriver_win32//chromedriver.exe") 
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
#navigate to the url  
driver.get("https://www.amazon.in/")  
#identify the user name text box and enter the value  
driver.find_element_by_id("twotabsearchtextbox").send_keys("ear buds")  
time.sleep(2) 
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(2)  
#driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/div[2]/div/div/div[1]/h2/a/span").click()
driver.get("https://www.amazon.in/Jabra-Elite-Active-Bluetooth-Earbuds/dp/B09FJJ2JXC/ref=sr_1_1_sspa?keywords=ear+buds&qid=1637749271&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyV1o0WDZYNjQ0TjA2JmVuY3J5cHRlZElkPUEwODQzMDk2MVhZN0ZMSU5WNTVaVSZlbmNyeXB0ZWRBZElkPUEwNDMxMTQ2MTVYRkNMQUVKNkU1MCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
time.sleep(2) 
driver.find_element_by_id("add-to-cart-button").click()
time.sleep(2)
driver.find_element_by_id("hlb-view-cart-announce").click()
time.sleep(2)
driver.close()  
print("successfully completed")