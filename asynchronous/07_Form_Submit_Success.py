"""
Learn to fill and submit a form with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Fill all the text field in Example form
4) Click on Click me! button
5) Verify user is taken to Selenium Tutorial redirect page
6) Close the browser
"""

import asyncio
from caqui.caqui import AsyncDriver
from caqui.by import By

async def demo():
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
    driver = AsyncDriver(remote, capabilities)

    # Maximize the browser window
    await driver.maximize_window()
    # Navigate to Qxf2 Tutorial page
    await driver.get("http://qxf2.com/selenium-tutorial-main")

    #KEY POINT: Code to fill forms
    # Find the name field and fill name
    name = await driver.find_element("xpath", "//input[@id='name']")
    await name.send_keys('Avinash')
    # Find the email field and fill your email
    await (await driver.find_element("xpath", "//input[@name='email']")).send_keys('avinash@qxf2.com')
    # Find the phone no field and fill phone no
    phone = await driver.find_element("id", "phone")
    await phone.send_keys('9999999999')
    # Identify the xpath for Click me button and click on it
    button = await driver.find_element("xpath", "//button[text()='Click me!']")
    await button.click()
    # Wait for the new page to load
    await asyncio.sleep(3)
    # Verify user is taken to Qxf2 tutorial redirect url
    if (driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect'):
        print("Success")
    else:
        print("Failure")

    # Close the browser
    driver.close()

if __name__ == "__main__":
    asyncio.run(demo())