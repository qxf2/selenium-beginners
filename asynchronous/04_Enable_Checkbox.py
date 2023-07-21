"""
Learn to select a checkbox using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Find the Checkbox element in the Example form and enable it
4) Close the browser
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
    await driver.get("http://qxf2.com/selenium-tutorial-main")

    # KEY POINT: Locate the checkbox and click on it
    checkbox = await driver.find_element("xpath", "//input[@type='checkbox']")
    await checkbox.click()

    # Pause the script for 3 sec so you can confirm the check box was selected
    await asyncio.sleep(3)

    # Close the browser window
    driver.close()

if __name__ == "__main__":
    asyncio.run(demo())