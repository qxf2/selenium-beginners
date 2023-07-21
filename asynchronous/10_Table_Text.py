"""
Learn to parse the text within each cell of a table

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Get all the fields from the table
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
    # Navigate to Qxf2 Tutorial page
    await driver.get("http://qxf2.com/selenium-tutorial-main")

    # KEY POINT: Logic to get the text in each cell of the table
    # Find the Example table element in the page
    table = await driver.find_element("xpath", "//table[@name='Example Table']")
    # Use find_elements_by_xpath method to get the rows in the table
    rows = await table.find_elements("xpath", "//tbody/descendant::tr")
    # Create a list to store the text
    result_data = []
    # Go to each row and get the no of columns and the navigate to column
    # Then get the text from each column
    for row in rows:
        # Find no of columns by getting the td elements in each row
        cols = await row.find_elements("tag name", "td")
        cols_data = []
        for j in range(0,len(cols)):
            # Get the text of each field
            cols_data.append(cols[j].text.encode('utf-8'))
        result_data.append(cols_data)

    # Print the result list
    print(result_data)

    # Pause the script for 3 sec
    await asyncio.sleep(3)

    # Close the browser
    driver.close()


if __name__ == "__main__":
    asyncio.run(demo())