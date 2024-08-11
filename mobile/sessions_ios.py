from appium import webdriver
from os import path


CUR_DIR = path.dirname(path.abspath(__file__)) #__file__ magic variable - what file are we in
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'
CAPS = {
    'platformName': 'iOS',
    'platformVersion': '17.5',
    'deviceName': 'iPhone 15',
    'automationName': 'XCUITest',
    'app': APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM, 
    desired_capabilities=CAPS)
driver.quit()

###Deprecation of desired_capabilities: In newer versions of Selenium and Appium, 
# the desired_capabilities parameter is deprecated. 
# While it might still work in some cases, it's no longer the recommended approach.