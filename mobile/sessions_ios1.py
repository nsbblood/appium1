from appium import webdriver
from appium.options.ios import XCUITestOptions
from os import path

# Define paths and capabilities
CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://127.0.0.1:4723'

# Set up optionsa
options = XCUITestOptions()
options.platform_name = 'iOS'
options.automation_name = 'XCUITest'
options.platform_version = '17.5'  # Use the version that matches your simulator
options.device_name = 'iPhone 15'  # Use the device name that matches your simulator
options.app = APP

# Initialize the driver
try:
    driver = webdriver.Remote(APPIUM, options=options)
    print("Session started successfully!")
    # Add your test steps here
finally:
    if 'driver' in locals():
        driver.quit()