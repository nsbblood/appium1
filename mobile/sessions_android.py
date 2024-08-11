from appium import webdriver
from appium.options.android import UiAutomator2Options
from os import path
import sys
import time

# Define paths and capabilities
CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://127.0.0.1:4723'

# Set up options
options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.device_name = 'Medium_Phone_Api_28'  # Use one of your available AVDs
options.app = APP

# Print some debug information
print(f"ANDROID_HOME: {path.expandvars('$ANDROID_HOME')}")
print(f"App path: {APP}")
print(f"Options: {options.to_capabilities()}")

time.sleep(1)
# Initialize the driver
try:
    time.sleep(1)
    driver = webdriver.Remote(APPIUM, options=options)
    print("Session started successfully!")
    # Add your test steps here
except Exception as e:
    time.sleep(1)
    print(f"An error occurred: {e}")
    print(f"Error type: {type(e).__name__}")
    print(f"Error details: {sys.exc_info()}")
finally:
    time.sleep(2)
    if 'driver' in locals():
        driver.quit()