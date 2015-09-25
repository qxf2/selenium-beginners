"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome driver
2) Navigate to Qxf2 Tutorial page
3) Find the Click me! button and click on it
4) Close the driver
"""
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")

# KEY POINT: Locate the button and click on it 
button  = driver.find_element_by_xpath("//button[text()='Click me!']") 
button.click()

# Pause the script to wait for page elements to load
time.sleep(3)

# Close the browser
driver.close()

