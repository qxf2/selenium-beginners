"""
We are trying the exercises on https://weathershopper.pythonanywhere.com

This is a practice script. It is linear because I am still learning how to code.
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def get_temperature():
    "Return the temperature shown"
    temperature = temperature_locator.text.encode('utf-8')
    temperature = temperature.split()[0]
    temperature = int(temperature)

    return temperature


def choose_product(temperature):
    "Choose either moisturizer or sunscreen"
    product = ''
    if temperature < 19:
        product = 'moisturizers'
    if temperature > 34:
        product = 'sunscreens'
    button = browser.find_element("xpath", f"//button[contains(text(),'Buy {product}')]")
    button.click()


browser = webdriver.Firefox()
browser.get("https://weathershopper.pythonanywhere.com")

try:
    temperature_locator = browser.find_element("id", "temperature")
except NoSuchElementException:
    print("Weather shopper did not load. Automation could not find the temperature element")
else:
    print("Weather shopper loaded")
    temperature = get_temperature()
    choose_product(temperature)

browser.close()
