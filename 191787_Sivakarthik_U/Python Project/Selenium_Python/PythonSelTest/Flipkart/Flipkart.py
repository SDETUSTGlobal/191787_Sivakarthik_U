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
driver.get("https://www.flipkart.com/")  
 
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
driver.find_element_by_name("q").send_keys("ear buds")  
time.sleep(2) 

driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(2)  

driver.get("https://www.flipkart.com/boat-airdopes-131-bluetooth-headset/p/itmf76c6f983fbca?pid=ACCFSDGXX3S6DVBG&lid=LSTACCFSDGXX3S6DVBGISMVSQ&marketplace=FLIPKART&q=ear+buds&store=0pm%2Ffcn&spotlightTagId=BestsellerId_0pm%2Ffcn&srno=s_1_4&otracker=search&otracker1=search&fm=SEARCH&iid=7d9e4599-996b-4c32-b45b-3c575648e7ad.ACCFSDGXX3S6DVBG.SEARCH&ppt=sp&ppn=sp&ssid=u4xccx6twg0000001637747710779&qH=bf539cbe8cbe03a3")
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[2]/div[5]/div/div[2]/div[1]/ul/li[6]/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button").click()
time.sleep(2)
driver.close()  
print("successfully completed")