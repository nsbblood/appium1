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
options.device_name = 'Medium_Phone_Api_28'  # Make sure this AVD matches the APK's ABI
options.app = APP

# Print some debug information
print(f"ANDROID_HOME: {path.expandvars('$ANDROID_HOME')}")
print(f"App path: {APP}")
print(f"Options: {options.to_capabilities()}")

time.sleep(1)
# Initialize the driver
try:
    driver = webdriver.Remote(APPIUM, options=options)
    print("Session started successfully!")
    # Add your test steps here
except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Error type: {type(e).__name__}")
    print(f"Error details: {sys.exc_info()}")
finally:
    time.sleep(2)
    if 'driver' in locals():
        driver.quit()
