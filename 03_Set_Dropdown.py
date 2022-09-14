"""
Learn to set dropdowns with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Set Gender to Male in the Example Form
4) Close the browser
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()

# Navigate to Qxf2 Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")

# KEY POINT: Identify the dropdown and click on it
dropdown_element = driver.find_element("xpath", "//button[@data-toggle='dropdown']")
dropdown_element.click()
# Sleep is one way to pause while the page elements load
time.sleep(1)

# KEY POINT: Locate a particular option and click on it
driver.find_element("xpath", "//a[text()='Male']").click()
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close()
