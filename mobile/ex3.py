from appium import webdriver

desired_caps = {
    'platformName': 'iOS',
    'platformVersion': '15.0',  # replace with your iOS version
    'deviceName': 'iPhone 13',  # replace with your virtual device name
    'automationName': 'XCUITest',
    'app': '/path/to/your/app.app'  # path to your app
}

driver = webdriver.Remote('http://localhost:4723', desired_caps)
