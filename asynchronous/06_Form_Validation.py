"""
Check for the presence of absence of page elements

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Find the Click me! button and click on it
4) Check for the validation message
5) Close the browser
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

    # Find the click me! button and click it
    button = await driver.find_element("xpath" ,"//button[text()='Click me!']")
    await button.click()
    # Pause the script to wait for validation messages to load
    await asyncio.sleep(3)

    # KEY POINT: Check if the validation mesage for name field
    try:
        await driver.find_element("xpath", "//label[text()='Please enter your name']")
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

if __name__ == "__main__":
    asyncio.run(demo())