from behave import *
from selenium import webdriver
@given(u'chrome is launched')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver_win32\chromedriver.exe")


@when(u'we navigate to Myntra website')
def step_impl(context):
    context.driver.get("https://www.myntra.com/")


@when(u'we enter product "Sunglasses" in search bar')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/input").send_keys("Sunglasses")




@when(u'we press the search button')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/header/div[2]/div[3]/a/span").click()


@then(u'we successfully navigate to the product list page')
def step_impl(context):


    context.driver.get("https://www.myntra.com/sunglasses/hrx-by-hrithik-roshan/hrx-by-hrithik-roshan-unisex-polarised-aviator-sunglasses-mfb-pn-cy-50563-c6/13129524/buy")