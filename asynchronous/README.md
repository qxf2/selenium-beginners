# Asynchronous calls

To perform asynchornous calls to WebDrivers you can use **Caqui**

## Simple start
Install the lastest version of **Caqui**

```
pip install -r requirements.txt
```

Download the same [ChromeDriver](https://chromedriver.chromium.org/downloads) version as your installed Chrome and start the Driver as a server using the port "9999"

```
$ ./chromedriver --port=9999
Starting ChromeDriver 94.0.4606.61 (418b78f5838ed0b1c69bb4e51ea0252171854915-refs/branch-heads/4606@{#1204}) on port 9999
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
```
Run the examples
```
python asynchronous/01_Navigate_Url.py
```

