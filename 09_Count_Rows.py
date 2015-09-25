"""
Learn to count the rows in a table using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Find the no of rows in the Example tabel
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

# Find the table element in the page
table = driver.find_element_by_xpath("//table[@name='Example Table']")

# KEY POINT: Find the tr elements in the table
rows = table.find_elements_by_xpath("//tbody/descendant::tr")
print "Total No of Rows: %d"%len(rows)

# Pause the script for 3 seconds
time.sleep(3)

# Close the browser
driver.close()
