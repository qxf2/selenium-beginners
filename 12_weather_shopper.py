"""
We are trying the exercises on https://weathershopper.pythonanywhere.com

This is a practice script. It is linear because I am still learning how to code.
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Firefox()
browser.get("https://weathershopper.pythonanywhere.com")

try:
    temperature_locator = browser.find_element("id", "temperature")
except NoSuchElementException:
    print("Weather shopper did not load. Automation could not find the temperature element")
else:
    print("Weather shopper loaded")

browser.close()
