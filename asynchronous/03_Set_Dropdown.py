"""
Learn to set dropdowns with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Set Gender to Male in the Example Form
4) Close the browser
"""
import asyncio
from caqui.caqui import AsyncDriver
from caqui.by import By

async def demo():
    # Create an instance of Firefox WebDriver
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

    # KEY POINT: Identify the dropdown and click on it
    dropdown_element = await driver.find_element("xpath", "//button[@data-toggle='dropdown']")
    await dropdown_element.click()
    # Sleep is one way to pause while the page elements load
    await asyncio.sleep(1)

    # KEY POINT: Locate a particular option and click on it
    await (await driver.find_element("xpath", "//a[text()='Male']")).click()
    # Future tutorials cover explicit, implicit and ajax waits
    await asyncio.sleep(3)

    # Close the browser window
    driver.close()
    print("Finished")

if __name__ == "__main__":
    asyncio.run(demo())