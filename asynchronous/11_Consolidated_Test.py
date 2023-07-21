"""
Selenium script that performs several common actions like:
click button, select dropdown, enable checkbox, set text, get text from table

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Print the contents of the table
4) Fill all the text fields
5) Select Dropdown option
6) Enable the checkbox
7) Take a screenshot
8) Click on Submit button
9) Close the browser
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

    # Find the Example table element in the page
    table = await driver.find_element("xpath", "//table[@name='Example Table']")
    # Find no of rows in the table by getting the tr elements in the table
    # Using find_elements_by_xpath method
    rows = await table.find_elements("xpath", "//tbody/descendant::tr")
    # Create a list to store the text
    result_data = []
    # Go to each row and get the no of columns and the navigate to column
    # Then get the text from each column
    for i in range(0,len(rows)):
        # Find no of columns by getting the td elements in each row
        cols = await rows[i].find_elements("tag name", "td")
        cols_data = []
        for j in range(0,len(cols)):
            # Get the text of each field
            cols_data.append(cols[j].text.encode('utf-8'))
        result_data.append(cols_data)
    # Print the result set
    print(result_data)

    # Find the name field using xpath with id
    name = await driver.find_element("xpath", "//input[@id='name']")
    # Send text to the name element using send_keys method
    await name.send_keys('Avinash')
    # Find the email field using xpath without id
    email = await driver.find_element("xpath", "//input[@name='email']")
    await email.send_keys('avinash@qxf2.com')
    # Find the phone no field using id
    phone = await driver.find_element("id", "phone")
    await phone.send_keys('9999999999')

    # Set a dropdown
    await (await driver.find_element("xpath", "//button[@data-toggle='dropdown']")).click()
    await asyncio.sleep(1)
    # Find the xpath of particular option and click on it
    await (await driver.find_element("xpath", "//a[text()='Male']")).click()

    # Set a checkbox
    checkbox = await driver.find_element("xpath", "//input[@type='checkbox']")
    await checkbox.click()

    # Take screenshot
    await driver.save_screenshot('Qxf2_Tutorial.png')

    # Identify the xpath for Click me button and click on it
    button = await driver.find_element("xpath", "//button[text()='Click me!']")
    await button.click()

    # Pause the script for 3 sec
    await asyncio.sleep(3)

    # Verify user is taken to Qxf2 tutorial redirect url
    print(driver.current_url)
    if (driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect'):
        print("Success")
    else:
        print("Failure")

    # Pause the script for 3 sec
    await asyncio.sleep(3)

    # Close the browser
    driver.close()


if __name__ == "__main__":
    asyncio.run(demo())