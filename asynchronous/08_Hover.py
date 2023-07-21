"""
Learn to hover over elements using Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Click on Menu icon
4) Hover over Resource and GUI automation and click on GUI automation link
5) Close the browser
"""


import asyncio
#Notice this extra import statement (ActionChains)!
from caqui.caqui import AsyncDriver, ActionChains
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

    # Locate the Menu icon and click on it
    menu = await driver.find_element("xpath", "//img[@src='./assets/img/menu.png']")
    await menu.click()

    # Locate the Resource element to hover over
    resource = await driver.find_element("xpath", "//a[text()='Resources']")

    # KEY POINT: Use ActionChains to hover over elements
    action = ActionChains(driver)
    action.move_to_element(resource)
    await action.perform()
    await asyncio.sleep(2) #Adding waits to make the example more visual

    # Click the GUI automation link
    gui_automation = await driver.find_element("xpath", "//a[text()='GUI automation']")
    await gui_automation.click()

    # Wait for 3 seconds for the page to load
    await asyncio.sleep(3)

    # Close the browser
    driver.close()

if __name__ == "__main__":
    asyncio.run(demo())