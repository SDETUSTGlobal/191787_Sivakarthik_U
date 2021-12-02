from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
print("Test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("D://Selenium//chromedriver_win32//chromedriver.exe") 
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
#navigate to the url  
driver.get("http://127.0.0.1:5000/")  
#identify the user name text box and enter the value
time.sleep(2)
driver.find_element_by_id("name").send_keys("Sivakarthik Unnikrishnan")  
time.sleep(2) 
driver.find_element_by_id("companyname").send_keys("UST")
time.sleep(2)
driver.find_element_by_id("UID").send_keys("342198")
time.sleep(2)
driver.find_element_by_id("EmailID").send_keys("siva@gmail.com")
time.sleep(2)
driver.find_element_by_id("buttonname").click()
time.sleep(2)
driver.close()  
print("Test successfully completed")