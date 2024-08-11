from appium import webdriver

desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '17.5',
    'deviceName': 'iPhone 15 Pro',
    'app': '/Users/enesarikan/Desktop/automation/python/appium1/mobile/TheApp.app.zip',
    'automationName': 'XCUITest'
}

# Explicitly specify the desired capabilities
driver = webdriver.Remote('http://localhost:4723', desired_caps)
driver.quit()