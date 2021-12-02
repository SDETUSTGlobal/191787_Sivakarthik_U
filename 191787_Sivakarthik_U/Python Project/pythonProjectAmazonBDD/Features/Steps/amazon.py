from behave import *
from selenium import webdriver
@given(u'chrome is launched')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\Selenium\chromedriver_win32\chromedriver.exe")


@when(u'we navigate to Amazon website')
def step_impl(context):
    context.driver.get("https://www.amazon.in/")


@when(u'we enter product "Ear buds" in search bar')
def step_impl(context):
    context.driver.find_element_by_id("twotabsearchtextbox").send_keys("Ear buds")




@when(u'we press the search button')
def step_impl(context):
    context.driver.find_element_by_id("nav-search-submit-button").click()


@then(u'we successfully navigate to the product list page')
def step_impl(context):
   context.driver.get("https://www.amazon.in/Noise-Buds-VS103-HyperSync-Technology/dp/B095YZB3MS/ref=sr_1_1_sspa?keywords=ear%2Bbuds&qid=1637853213&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRURUWUJMMEhFMzdHJmVuY3J5cHRlZElkPUEwNzQ4MjA3RDVZRVA4SEdZTU80JmVuY3J5cHRlZEFkSWQ9QTA5NTk2MzBMWlNQTkhBS1gxMFkmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1")
