"""
Learn to fill and submit a form with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Fill all the text field in Example form
4) Click on Click me! button
5) Verify user is taken to Selenium Tutorial redirect page
6) Close the browser
"""

import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")

#KEY POINT: Code to fill forms
# Find the name field and fill name
name = driver.find_element_by_xpath("//input[@id='name']")  
name.send_keys('Avinash')
# Find the email field and fill your email
driver.find_element_by_xpath("//input[@name='email']").send_keys('avinash@qxf2.com')
# Find the phone no field and fill phone no
phone = driver.find_element_by_id('phone')
phone.send_keys('9999999999')
# Identify the xpath for Click me button and click on it 
button = driver.find_element_by_xpath("//button[text()='Click me!']")  
button.click()
# Wait for the new page to load
time.sleep(3)
# Verify user is taken to Qxf2 tutorial redirect url
if (driver.current_url== 'http://qxf2.com/selenium-tutorial-redirect'):
    print "Success"
else:
    print "Failure"

# Close the browser   
driver.close()
        

