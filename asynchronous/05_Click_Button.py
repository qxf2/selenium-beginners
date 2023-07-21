"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Chrome driver
2) Navigate to Qxf2 Tutorial page
3) Find the Click me! button and click on it
4) Close the driver
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

    # KEY POINT: Locate the button and click on it
    button  = await driver.find_element("xpath", "//button[text()='Click me!']")
    await button.click()

    # Pause the script to wait for page elements to load
    await asyncio.sleep(3)

    # Close the browser
    driver.close()

if __name__ == "__main__":
    asyncio.run(demo())