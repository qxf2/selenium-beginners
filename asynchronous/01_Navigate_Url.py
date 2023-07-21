"""
Learn to navigate to a URL using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Check the page title
4) Close the browser
"""
from caqui.caqui import AsyncDriver
from caqui.by import By
import asyncio

# Create an instance of WebDriver
# To run the webdriver, run "./chromedriver --port=9999"
remote = "http://127.0.0.1:9999"
capabilities = {
    "desiredCapabilities": {
        By.NAME: "webdriver",
        "browserName": "chrome",
        "acceptInsecureCerts": True,
        # "goog:chromeOptions": {"extensions": [], "args": ["--headless"]},
    }
}
browser = AsyncDriver(remote, capabilities)

# KEY POINT: The driver.get method will navigate to a page given by the URL
get_task = browser.get('http://qxf2.com/selenium-tutorial-main')
asyncio.run(get_task)

# Check if the title of the page is proper
if(browser.title=="Qxf2 Services: Selenium training main"):
    print ("Success: Qxf2 Tutorial page launched successfully")
else:
    print ("Failed: Qxf2 Tutorial page Title is incorrect")

# Quit the browser window
browser.quit()
