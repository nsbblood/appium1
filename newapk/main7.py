from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import os
import traceback
import time

# Configuration
current_dir = os.path.dirname(__file__)
apk_path = os.path.join(current_dir, 'ApiDemos-debug.apk')
screenshot_dir = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/screenshots4"
text_file_path = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/text3.txt"

os.makedirs(screenshot_dir, exist_ok=True)

# Appium setup
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

def safe_click(element):
    try:
        element.click()
        return True
    except (NoSuchElementException, StaleElementReferenceException):
        return False

def get_element_details(element):
    try:
        text = element.text
        content_desc = element.get_attribute('content-desc')
        class_name = element.get_attribute('class')
        return f"{text or content_desc or 'Unnamed'} ({class_name})"
    except StaleElementReferenceException:
        return "Stale Element"

def analyze_page():
    elements = []
    for elem_type in ["android.widget.TextView", "android.widget.Button", "android.widget.EditText", "android.widget.ImageView", "android.widget.CheckBox", "android.widget.RadioButton", "android.widget.Switch"]:
        items = driver.find_elements(AppiumBy.CLASS_NAME, elem_type)
        if items:
            elements.extend([get_element_details(item) for item in items])
    return elements

def write_to_file(name, elements, indent=""):
    with open(text_file_path, "a") as file:
        file.write(f"\n{indent}--- {name} ---\n")
        for element in elements:
            file.write(f"{indent}{element}\n")

def interact_with_element(element):
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element))
        class_name = element.get_attribute('class')
        if class_name in ['android.widget.CheckBox', 'android.widget.RadioButton', 'android.widget.Switch']:
            element.click()
            time.sleep(1)
            element.click()  # Toggle back to original state
        elif class_name == 'android.widget.EditText':
            element.send_keys("Test Input")
            time.sleep(1)
            element.clear()
        else:
            element.click()
        time.sleep(2)
    except StaleElementReferenceException:
        print("Element went stale, re-locating and retrying...")
        re_located_element = driver.find_element(AppiumBy.XPATH, "//*[@clickable='true' and text()='{}']".format(element.text))
        interact_with_element(re_located_element)

def explore_category(category_name, depth=0, max_depth=5):
    if depth > max_depth:
        return

    indent = "  " * depth
    print(f"{indent}Exploring: {category_name}")

    screenshot_path = os.path.join(screenshot_dir, f"{'_'.join(category_name.split())}_depth{depth}.png")
    driver.get_screenshot_as_file(screenshot_path)

    page_elements = analyze_page()
    write_to_file(category_name, page_elements, indent)

    clickable_elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")

    for element in clickable_elements:
        element_name = get_element_details(element)
        print(f"{indent}  Interacting with: {element_name}")
        
        interact_with_element(element)
        
        try:
            WebDriverWait(driver, 5).until(EC.staleness_of(element))
            explore_category(element_name, depth + 1, max_depth)
        except TimeoutException:
            print(f"{indent}    No new page loaded, continuing...")
        
        if depth > 0:  # Don't go back from the main page
            try:
                driver.back()
                time.sleep(2)
            except:
                print(f"{indent}  Could not go back from: {element_name}")

def main():
    try:
        main_categories = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        for category in main_categories:
            category_name = category.text
            if safe_click(category):
                explore_category(category_name)
                driver.back()
                time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
#!!!! check it again
