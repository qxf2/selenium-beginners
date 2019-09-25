"""
Check for the presence of absence of page elements

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Internet Explorer driver
2) Navigate to Qxf2 Tutorial page
3) Find the Click me! button and click on it
4) Check for the validation message
5) Close the browser
"""
import time
import os
from selenium import webdriver

# Create an instance of MS Edge WebDriver
# dir = os.path.dirname(__file__)
# edge_path = dir + "\\msedgedriver.exe"
driver=webdriver.Ie()
# driver = webdriver.Edge(executable_path="C:\\Program Files (x86)\\MicrosoftWebDriver\\MicrosoftWebDriver.exe")
#driver=webdriver.Edge(executable_path="C:\\Users\\Rahul Bhave Qxf2\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\msedgedriver.exe")
# Maximize the browser window
driver.maximize_window()
# time.sleep(250)
# Navigate to Qxf2 Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")


# Find the click me! button and click it
time.sleep(10)
button  = driver.find_element_by_xpath("//button[text()='Click me!']")  
button.click()
# Pause the script to wait for validation messages to load
time.sleep(3)

# KEY POINT: Check if the validation mesage for name field
try:
    driver.find_element_by_xpath("//label[text()='Please enter your name']")
except Exception as e:
    #This pattern of catching all exceptions is ok when you are starting out
    result_flag = False 
else:
    result_flag = True
if result_flag is True:
    print("Validation message for name present")
else:
    print("Validation message for name NOT present")

# Close the browser window
driver.close()


    
