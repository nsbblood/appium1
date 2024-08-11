from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.ios import XCUITestOptions
from os import path

# Define paths and capabilities
CUR_DIR = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

# Set up options
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
    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_all_elements_located(
        (AppiumBy.ACCESSIBILITY_ID, 'Login Screen')
    ))
    driver.find_element(AppiumBy.CLASS_NAME,'XCUIElementTypeStaticText')
    driver.find_element(AppiumBy.XPATH,'//XCUIElementTypeOther[@label="Webview Demo"]')
finally:
        driver.quit()


