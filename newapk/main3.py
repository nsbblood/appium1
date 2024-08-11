from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import traceback
import time

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

current_dir = os.path.dirname(__file__)
apk_path = os.path.join(current_dir, 'ApiDemos-debug.apk')
screenshot_dir = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/screenshots" #create a file named screenshots

# Ensure the screenshot directory exists
os.makedirs(screenshot_dir, exist_ok=True)

options = AppiumOptions()
options.load_capabilities({
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "9.0",
    "appium:deviceName": "Medium_Phone_API_28",
    "appium:app": apk_path,
    "appium:newCommandTimeout": 3600,
    "appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 10)

def click_and_screenshot(element, name):
    element.click()
    time.sleep(2)  # Wait for the click action to complete
    screenshot_path = os.path.join(screenshot_dir, f"{name}_screenshot.png")
    driver.get_screenshot_as_file(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    time.sleep(5)  # Additional wait after screenshot

try:
    menu_items = [
        ("Access'ibility", "accessibility"),
        ("Animation", "animation"),
        ("App", "app"),
        ("Content", "content"),
        ("Graphics", "graphics"),
        ("Media", "media"),
        ("NFC", "nfc"),
        ("OS", "os"),
        ("Preference", "preference"),
        ("Views", "views"),
        ("Text", "text")
    ]

    for item_name, screenshot_name in menu_items:
        menu_item = wait.until(
            EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, item_name))
        )
        print(f"{item_name} menu is visible")
        click_and_screenshot(menu_item, screenshot_name)
        
        if item_name != "Text":
            driver.back()
        else:
            # For "Text" menu, navigate to "LogTextBox"
            menu_text_longtextbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "LogTextBox"))
            )
            print("LogTextBox menu is visible")
            click_and_screenshot(menu_text_longtextbox, "logtextbox")

            field_longtextbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/text"))
            )
            print("LongTextBox field is visible")
            field_longtextbox.click()
            field_longtextbox.send_keys("jonathan hermawan")
            
            add_longtextbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Add"))
            )
            print("Add button is visible")
            click_and_screenshot(add_longtextbox, "add_button")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()


#defined a function
#It saves eash screenshots to a folder that we want
