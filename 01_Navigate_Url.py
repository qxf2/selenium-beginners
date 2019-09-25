"""
Learn to navigate to a URL using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Check the page title
4) Close the browser
"""
from selenium import webdriver

# Create an instance of Firefox WebDriver
# browser = webdriver.Firefox(executable_path="C:\\geckodriver\\geckodriver.exe")
browser=webdriver.Firefox()

# KEY POINT: The driver.get method will navigate to a page given by the URL
browser.get('http://qxf2.com/selenium-tutorial-main')

# Check if the title of the page is proper
if(browser.title=="Qxf2 Services: Selenium training main"):
    print ("Success: Qxf2 Tutorial page launched successfully")
else:
    print ("Failed: Qxf2 Tutorial page Title is incorrect") 

# Quit the browser window
browser.quit() 
