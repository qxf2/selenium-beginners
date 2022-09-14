"""
Learn to hover over elements using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Click on Menu icon
4) Hover over Resource and GUI automation and click on GUI automation link
5) Close the browser
"""

import time
from selenium import webdriver

#Notice this extra import statement!
from selenium.webdriver.common.action_chains import ActionChains

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")

# Locate the Menu icon and click on it
menu = driver.find_element("xpath", "//img[@src='./assets/img/menu.png']")
menu.click()

# Locate the Resource element to hover over
resource = driver.find_element("xpath", "//a[text()='Resources']")

# KEY POINT: Use ActionChains to hover over elements
action = ActionChains(driver)
action.move_to_element(resource)
action.perform()
time.sleep(2) #Adding waits to make the example more visual

# Click the GUI automation link
gui_automation = driver.find_element("xpath", "//a[text()='GUI automation']")
gui_automation.click()

# Wait for 3 seconds for the page to load
time.sleep(3)

# Close the browser
driver.close()
