from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from os import path

# Define paths and capabilities
CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

# Set up options
options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.device_name = 'Small_Phone_Api_35'  # Update this to your ARM64 emulator name
options.app = APP
options.avd = 'Small_Phone_Api_35'  # Add this line with your emulator name

# Additional options that might be helpful
options.new_command_timeout = 60
options.app_wait_activity = '*'

# Initialize the driver
try:
    driver = webdriver.Remote(APPIUM, options=options)
    print("Session started successfully!")
    # Add your test steps here
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located(
        (AppiumBy.ACCESSIBILITY_ID, 'Login Screen')
    ))
    driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')
    driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@text="Webview Demo"]')
finally:
    if 'driver' in locals():
        driver.quit()