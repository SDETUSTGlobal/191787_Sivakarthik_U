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
driver.get("https://www.myntra.com/")  
 
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("Wallets")

time.sleep(2) 

driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span").click()
time.sleep(2)
driver.get("https://www.myntra.com/wallets/peter-england/peter-england-men-black-leather-two-fold-wallet/14881770/buy")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/main/div[2]/div[2]/div[3]/div/div[1]").click()
driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[2]/a[2]/span[3]").click()
print("Program successfull")
driver.close()