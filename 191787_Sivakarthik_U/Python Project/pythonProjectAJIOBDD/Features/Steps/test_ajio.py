from behave import *
from selenium import webdriver
@given(u'chrome is launched')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver_win32\chromedriver.exe")


@when(u'we navigate to Ajio website')
def step_impl(context):
    context.driver.get("https://www.ajio.com/")


@when(u'we enter product "Sunglasses" in search bar')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/div/input").send_keys("Sunglasses")




@when(u'we press the search button')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/button/span").click()


@then(u'we successfully navigate to the product list page')
def step_impl(context):

    #context.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/button/span").click()
    context.driver.get("https://www.ajio.com/love-moschino-mol035-s-full-rim-square-sunglasses/p/460915713_grey")