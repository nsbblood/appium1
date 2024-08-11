from appium import webdriver

desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '17.5',  # Adjust to your iOS version
    'deviceName': 'iPhone 15 Pro',  # Adjust to your device name
    'automationName': 'XCUITest',  # Specifies the automation engine
    'app': '/Users/enesarikan/Desktop/automation/python/appium1/mobile/TheApp.app.zip'  # Path to your app
}

driver = webdriver.Remote('http://localhost:4723', desired_caps) #

driver.quit()

