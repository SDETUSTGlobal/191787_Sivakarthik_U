import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

MYNTRA_HOME = 'https://www.myntra.com/'

# Scenarios

scenarios('../test_Myntra.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path="D:\Selenium\chromedriver_win32\chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('the Myntra home page is displayed')
def ddg_home(browser):
    browser.get(MYNTRA_HOME)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_xpath('/html/body/div[1]/div/div/header/div[2]/div[3]/input')
    search_input.send_keys(phrase)
    search = browser.find_element_by_xpath('/html/body/div[1]/div/div/header/div[2]/div[3]/a/span')
    search.click()


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):

    search_input = browser.get('https://www.myntra.com/shirts/roadster/roadster-men-blue-printed-casual-shirt/1364628/buy')
