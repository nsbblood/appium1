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

try:
    menu_accessibility = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Access'ibility"))
    )
    time.sleep(2)
    print("Access'ibility menu is visible")
    menu_accessibility.click()

    driver.back()

    menu_text = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Text"))
    )
    time.sleep(2)

    print("Text menu is visible")
    menu_text.click()

    menu_text_longtextbox = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "LogTextBox"))
    )
    time.sleep(2)

    print("LogTextBox menu is visible")
    menu_text_longtextbox.click()

    field_longtextbox = wait.until(
        EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/text"))
    )
    time.sleep(2)

    print("LongTextBox field is visible")
    field_longtextbox.click()
    field_longtextbox.send_keys("jonathan hermawan")

    add_longtextbox = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Add"))
    )
    time.sleep(2)

    print("Add button is visible")
    add_longtextbox.click()

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()