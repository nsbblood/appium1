from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import os
import traceback
import time

# Configuration
current_dir = os.path.dirname(__file__)
apk_path = os.path.join(current_dir, 'ApiDemos-debug.apk')
screenshot_dir = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/screenshots3"
text_file_path = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/text1.txt"

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
    """Attempt to click an element safely."""
    try:
        element.click()
        return True
    except (NoSuchElementException, StaleElementReferenceException):
        return False

def get_element_details(element):
    """Extract relevant details from an element."""
    try:
        text = element.text
        content_desc = element.get_attribute('content-desc')
        class_name = element.get_attribute('class')
        return f"{text or content_desc or 'Unnamed'} ({class_name})"
    except StaleElementReferenceException:
        return "Stale Element"

def analyze_page():
    """Analyze the current page and return a list of element details."""
    elements = []
    
    for elem_type in ["android.widget.Button", "android.widget.TextView", "android.widget.EditText"]:
        items = driver.find_elements(AppiumBy.CLASS_NAME, elem_type)
        if items:
            elements.append(f"{elem_type.split('.')[-1]}s found:")
            elements.extend([f"- {get_element_details(item)}" for item in items])
    
    images = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
    if images:
        elements.append(f"Images found: {len(images)}")
    
    return elements if elements else ["No interactive elements found"]

def write_to_file(name, elements, indent=""):
    """Write the analyzed elements to the text file."""
    with open(text_file_path, "a") as file:
        file.write(f"\n{indent}--- {name} ---\n")
        for element in elements:
            file.write(f"{indent}{element}\n")

def explore_and_analyze(name, depth=0, max_depth=3):
    """Recursively explore and analyze pages."""
    if depth > max_depth:
        return

    indent = "  " * depth
    print(f"{indent}Exploring: {name}")
    
    screenshot_path = os.path.join(screenshot_dir, f"{'_'.join(name.split())}_depth{depth}.png")
    driver.get_screenshot_as_file(screenshot_path)
    
    page_elements = analyze_page()
    write_to_file(name, page_elements, indent)

    clickable_elements = driver.find_elements(AppiumBy.XPATH, "//*[@clickable='true']")
    
    for element in clickable_elements:
        element_name = get_element_details(element)
        if safe_click(element):
            time.sleep(2)  # Wait for page to load
            explore_and_analyze(element_name, depth + 1, max_depth)
            driver.back()
            time.sleep(2)  # Wait for previous page to reload

def main():
    try:
        explore_and_analyze("Main Menu")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

#It could not complete all the steps.First steps are tested but second steps stoped working...
