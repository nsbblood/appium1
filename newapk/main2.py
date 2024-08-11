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
    time.sleep(5)
    print("Access'ibility menu is visible")
    menu_accessibility.click()
    time.sleep(7)

    driver.back()

    menu_acc = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Animation"))
    )
    time.sleep(5)
    print("Animation menu is visible")
    menu_acc.click()
    time.sleep(7)
    driver.back()

    menu_apps = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "App"))
    )
    time.sleep(5)
    print("Apps menu is visible")
    menu_apps.click()
    time.sleep(7)
    driver.back()

    menu_content = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Content"))
    )
    time.sleep(5)
    print("Content menu is visible")
    menu_content.click()
    time.sleep(7)
    driver.back()

    menu_graphics = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Graphics"))
    )
    time.sleep(5)
    print("Graphics menu is visible")
    menu_graphics.click()
    time.sleep(7)
    driver.back()

    menu_media = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Media"))
    )
    time.sleep(5)
    print("Media menu is visible")
    menu_media.click()
    time.sleep(7)
    driver.back()

    menu_nfc = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "NFC"))
    )
    time.sleep(5)
    print("Graphics menu is visible")
    menu_nfc.click()
    time.sleep(7)
    driver.back()

    menu_os = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "OS"))
    )
    time.sleep(5)
    print("Graphics menu is visible")
    menu_os.click()
    time.sleep(7)
    driver.back()

    menu_preference = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Preference"))
    )
    time.sleep(5)
    print("Graphics menu is visible")
    menu_preference.click()
    time.sleep(7)
    driver.back()

    menu_views = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Views"))
    )
    time.sleep(5)
    print("Graphics menu is visible")
    menu_views.click()
    time.sleep(7)
    driver.back()


    menu_text = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Text"))
    )
    time.sleep(2)
    print("Text menu is visible")
    time.sleep(7)
    menu_text.click()

    menu_text_longtextbox = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "LogTextBox"))
    )
    time.sleep(3)

    print("LogTextBox menu is visible")
    menu_text_longtextbox.click()

    time.sleep(7)
    field_longtextbox = wait.until(
        EC.visibility_of_element_located((AppiumBy.ID, "io.appium.android.apis:id/text"))
    )
    time.sleep(2)

    print("LongTextBox field is visible")
    field_longtextbox.click()
    field_longtextbox.send_keys("jonathan hermawan")
    time.sleep(7)
    add_longtextbox = wait.until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Add"))
    )
    time.sleep(2)

    print("Add button is visible")
    add_longtextbox.click()
    time.sleep(7)
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()