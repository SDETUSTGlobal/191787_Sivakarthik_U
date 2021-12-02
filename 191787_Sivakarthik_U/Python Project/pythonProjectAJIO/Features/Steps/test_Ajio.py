import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

AJIO_HOME = 'https://www.ajio.com/'

# Scenarios

scenarios('../findAjio.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome(executable_path="D:\Selenium\chromedriver_win32\chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('the Ajio home page is displayed')
def ddg_home(browser):
    browser.get(AJIO_HOME)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/div/input')
    search_input.send_keys(phrase)
    search = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/header/div[3]/div[2]/form/div/button/span')
    search.click()


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):

    search_input = browser.get('https://www.ajio.com/dennislingo-premium-attire--slim-fit-shirt-with-spread-collar/p/462323964_black')
