"""
Learn to fill text fields with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Douglas Cardoso
Contact: https://github.com/douglasdcm

SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Find elements using id, xpath, xpath without id
4) Fill name, email and phone no in the respective fields
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

    # The driver.get method will navigate to a page given by the URL
    driver = AsyncDriver(remote, capabilities)
    await driver.get("http://qxf2.com/selenium-tutorial-main")

    # Check if the title of the page is proper
    if(driver.title=="Qxf2 Services: Selenium training main"):
        print ("Success: Qxf2 Tutorial page launched successfully")
    else:
        print ("Failure: Qxf2 Tutorial page Title is incorrect")

    # Find the name field using xpath with id
    name = driver.find_element(By.XPATH, "//input[@id='name']")
    
    # Find the email field using xpath without id
    email = driver.find_element(By.XPATH, "//input[@name='email']")
    
    # Find the phone no field using id
    phone = driver.find_element("id", "phone")
    
    # Run all commands concurrently 
    name, email, phone = await asyncio.gather(name, email, phone)

    # KEY POINT: Send text to an element using send_keys method
    await asyncio.gather(
        name.send_keys('Avinash'),
        email.send_keys('avinash@qxf2.com'),
        phone.send_keys('9999999999'),
    )

    # Sleep is one way to wait for things to load
    # Future tutorials cover explicit, implicit and ajax waits
    await asyncio.sleep(3)

    # Close the browser window
    driver.close()

if __name__ == "__main__":
    asyncio.run(demo())