from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome("D://Selenium//chromedriver_win32//chromedriver.exe")
#maximize the window size  
driver.maximize_window()  
#delete the cookies  
driver.delete_all_cookies()  
driver.get("http://secure.smartbearsoftware.com/samples/testcomplete11/WebOrders/login.aspx");
driver.find_element_by_id("ctl00_MainContent_username").send_keys("Tester");
time.sleep(3)
driver.find_element_by_id("ctl00_MainContent_password").send_keys("test");
time.sleep(3)
driver.find_element_by_id("ctl00_MainContent_login_button").click();
driver.find_element_by_id("ctl00_MainContent_btnCheckAll").click();
       
driver.find_element_by_id("ctl00_MainContent_btnDelete").click();
driver.find_element_by_id("ctl00_MainContent_orderLInk").click();
driver.back();
driver.back();
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click();
driver.find_element_by_id("ctl00_MainContent_orderGrid_ctl02_OrderSelector").click();
driver.find_element_by_id("ctl00_MainContent_btnUncheckAll").click();
driver.find_element_by_link_text("View all products").click();
driver.find_element_by_partial_link_text("Order").click();
driver.find_element_by_css_selector("#ctl00_MainContent_fmwOrder_txtQuantity").send_keys("1111");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtUnitPrice").send_keys("33");
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click();
       
driver.find_element_by_name("ctl00$MainContent$fmwOrder$txtName").send_keys("Sivakarthik");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("Panangad");

driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("Ernakulam");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("Kerala");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("612345");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_0").click();
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("9876543210");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("01/99");


driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click()
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/input").click();

dropdown = Select(driver.find_element_by_id("ctl00_MainContent_fmwOrder_ddlProduct"));  
dropdown.select_by_visible_text("FamilyAlbum");
driver.find_element_by_css_selector("#ctl00_MainContent_fmwOrder_txtQuantity").send_keys("9999");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_txtUnitPrice").send_keys("55");
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/ol[1]/li[5]/input[2]").click();
       
driver.find_element_by_name("ctl00$MainContent$fmwOrder$txtName").send_keys("Gangadhar");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox2").send_keys("Kadavanthra");

driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox3").send_keys("Ernakulam");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox4").send_keys("Kerala");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox5").send_keys("614325");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_cardList_0").click();
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox6").send_keys("5467893214");
driver.find_element_by_id("ctl00_MainContent_fmwOrder_TextBox1").send_keys("12/99");
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[2]/table/tbody/tr/td/div/a").click();
driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div[1]/span/a").click();
time.sleep(3)
print("Run Successfully")
driver.close()