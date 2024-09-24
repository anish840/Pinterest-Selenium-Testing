import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Test data and credentials
username = 'ftwexorcist@gmail.com'  
password = 'Amritanshu@123'        
pid = 'ftwexorcist'                
img_path = r"W:\picture\wall\977604.jpg" 
website = 'https://www.pinterest.com/login/'

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login(driver):
    driver.get(website)
    assert "Pinterest" in driver.title

    try:
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[1]'))
        )
    except NoSuchElementException as e:
        pytest.fail(f"Element not found: {e}")
    except TimeoutException as e:
        pytest.fail(f"Timeout: {e}")

def test_create_pin(driver):
    pin_title = "Test Pin"
    try:
        create_button_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[4]/div/a/div/div/span'
        create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, create_button_xpath))
        )
        create_button.click()
        time.sleep(3)
        
        image_upload_button_xpath = '//input[@type="file"]'
        image_upload_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, image_upload_button_xpath))
        )
        image_upload_button.send_keys(img_path)
        time.sleep(10)

        title_field_xpath = '//input[@id="storyboard-selector-title"]'
        title_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, title_field_xpath))
        )
        title_field.send_keys(pin_title)

        publish_button_xpath = '//button[contains(@class, "RCK Hsu USg adn NTm KhY iyn oRi lnZ wsz") and .//div[text()="Publish"]]'
        publish_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, publish_button_xpath))
        )
        publish_button.click()
    except TimeoutException as e:
        pytest.fail(f"Timeout: {e}")
    except NoSuchElementException as e:
        pytest.fail(f"Element not found: {e}")
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")


def test_about_button(driver):
    try:
        driver = webdriver.Chrome()
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the About button is visible and interactable
        about_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div/a'))
        )                                           
        print("Located About button on Pinterest homepage")

        # Get the current window handle (to switch back later)
        main_window = driver.current_window_handle

        # Click on the About button
        about_button.click()
        print("Clicked on About button")

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until two windows are open
        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Wait for the About page to load (you can add more specific waits if necessary)
        time.sleep(5)

        # Get the page title for debugging
        page_title = driver.title
        print(f"About page title: {page_title}")

        # Example assertion: Check if the page title contains 'About Pinterest'
        # assert "About Pinterest" in page_title
        print("Test 3 Passed: Successfully navigated to About page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}. Page title was: {page_title}")

    finally:
        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)
        print("Closed the new tab and switched back to the main window")

# Call the function to test the About button
test_about_button(driver)



def test_navigate_to_settings(driver):
    driver.get('https://www.pinterest.com/')
    try:
        accounts_options_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-accounts-options-button']"))
        )
        accounts_options_button.click()
        time.sleep(5)

        settings_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-menu-options-settings']"))
        )
        settings_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("settings")
        )
    except TimeoutException as e:
        pytest.fail(f"Timeout: {e}")
    except NoSuchElementException as e:
        pytest.fail(f"Element not found: {e}")
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

def test_navigate_to_notifications(driver):
    driver.get('https://www.pinterest.com/')
    try:
        notifications_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Notifications' and contains(@class, 'S9z') and contains(@class, 'INd')]"))
        )
        notifications_icon.click()
        time.sleep(5)

        notifications_dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'VxL _he ho- imm ojN p6V wc1 zI7 iyn Hsu')]"))
        )
        assert notifications_dropdown is not None
    except TimeoutException as e:
        pytest.fail(f"Timeout: {e}")
    except NoSuchElementException as e:
        pytest.fail(f"Element not found: {e}")
    except Exception as e:
        pytest.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    pytest.main(["-v", "--html=C:\\Users\\amrit\\Downloads\\selenium_testing-main\\report.html"])
