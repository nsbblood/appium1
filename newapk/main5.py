from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import traceback
import time

current_dir = os.path.dirname(__file__)
apk_path = os.path.join(current_dir, 'ApiDemos-debug.apk')
screenshot_dir = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/screenshots4"
text_file_path = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/text4.txt"

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

def click_and_analyze(element, name):
    element.click()
    time.sleep(2)
    screenshot_path = os.path.join(screenshot_dir, f"{name}_screenshot.png")
    driver.get_screenshot_as_file(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")
    
    page_elements = analyze_page()
    write_to_file(name, page_elements)
    
    time.sleep(5)

def analyze_page():
    elements = []
    
    # Check for all clickable elements
    clickable_elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
    if clickable_elements:
        elements.append("Clickable elements found:")
        for elem in clickable_elements:
            elem_text = elem.text or elem.get_attribute('content-desc')
            elem_class = elem.get_attribute('class')
            if elem_text:
                elements.append(f"- {elem_text} ({elem_class})")
            else:
                elements.append(f"- Unnamed {elem_class}")
    
    # Check for text views (which might be headers or menu items)
    text_views = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    if text_views:
        elements.append("Text elements found:")
        for text_view in text_views:
            text = text_view.text or text_view.get_attribute('content-desc')
            if text:
                elements.append(f"- {text}")
    
    # Check for input areas
    inputs = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    if inputs:
        elements.append("Input areas found:")
        for input_area in inputs:
            elements.append(f"- {input_area.get_attribute('content-desc') or input_area.text or 'Unnamed input'}")
    
    # Check for images
    images = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
    if images:
        elements.append(f"Images found: {len(images)}")
    
    # If no elements found, it might be a blank page
    if not elements:
        elements.append("Blank page or no interactive elements found")
    
    return elements

def write_to_file(name, elements):
    with open(text_file_path, "a") as file:
        file.write(f"\n\n--- {name} ---\n")
        for element in elements:
            file.write(f"{element}\n")

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
        click_and_analyze(menu_item, screenshot_name)
        
        if item_name != "Text":
            driver.back()
        else:
            # For "Text" menu, navigate to "LogTextBox"
            menu_text_longtextbox = wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "LogTextBox"))
            )
            print("LogTextBox menu is visible")
            click_and_analyze(menu_text_longtextbox, "logtextbox")

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
            click_and_analyze(add_longtextbox, "add_button")

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()


#This will also add categories(buttons) to text files. 