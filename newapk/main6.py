from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import AppiumOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
import os
import traceback
import time

current_dir = os.path.dirname(__file__)
apk_path = os.path.join(current_dir, 'ApiDemos-debug.apk')
screenshot_dir = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/screenshots5"
text_file_path = "/Users/enesarikan/Desktop/automation/python/appium1/newapk/text5.txt"

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

def analyze_page():
    elements = []
    
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
    
    text_views = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    if text_views:
        elements.append("Text elements found:")
        for text_view in text_views:
            text = text_view.text or text_view.get_attribute('content-desc')
            if text:
                elements.append(f"- {text}")
    
    inputs = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
    if inputs:
        elements.append("Input areas found:")
        for input_area in inputs:
            elements.append(f"- {input_area.get_attribute('content-desc') or input_area.text or 'Unnamed input'}")
    
    images = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.ImageView")
    if images:
        elements.append(f"Images found: {len(images)}")
    
    if not elements:
        elements.append("Blank page or no interactive elements found")
    
    return elements

def write_to_file(name, elements, indent=""):
    with open(text_file_path, "a") as file:
        file.write(f"\n\n{indent}--- {name} ---\n")
        for element in elements:
            file.write(f"{indent}{element}\n")

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
        element_text = element.text or element.get_attribute('content-desc')
        if not element_text:
            continue

        print(f"{indent}  Clicking: {element_text}")
        try:
            element.click()
            time.sleep(2)

            # Check if we've navigated to a new page
            try:
                WebDriverWait(driver, 5).until(EC.staleness_of(element))
                explore_category(element_text, depth + 1, max_depth)
            except TimeoutException:
                print(f"{indent}  No navigation occurred for: {element_text}")

            driver.back()
            time.sleep(2)
        except (NoSuchElementException, StaleElementReferenceException):
            print(f"{indent}  Element became stale: {element_text}")

def main():
    try:
        main_categories = [
            "Access'ibility", "Animation", "App", "Content", "Graphics",
            "Media", "NFC", "OS", "Preference", "Views", "Text"
        ]

        for category in main_categories:
            category_element = wait.until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, category))
            )
            category_element.click()
            time.sleep(2)
            
            explore_category(category)
            
            driver.back()
            time.sleep(2)

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        driver.quit()

if __name__ == "__main__":
    main()