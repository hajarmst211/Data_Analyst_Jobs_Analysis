# driver.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging


def verify_you_are_human(driver):
    #when called this function must be wrapped into a try-except TimeoutExeption block
        WebDriverWait(driver, timeout=300).until(EC.frame_to_be_available_and_switch_to_it('iframe_name_or_id'))

        btn = driver.find_element(By.XPATH, '//*[@id="GjRM0"]/div/label/input')

        action = ActionChains(driver)
        action.click_and_hold(btn)

        action.perform()

        time.sleep(10)

        action.release(btn)


def click_verification(driver):
    checkboxes = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
    target_checkbox = checkboxes[1] 
    target_checkbox.click()
    
def click_search_button(driver):
    try:
        span_element = driver.find_element(By.ID, "mySpan")
        button_element = span_element.find_element(By.TAG_NAME, "button")
        button_element.click()
    except Exception as e:
        logging.error(e)

    time.sleep(60*60)
    return 0
    
    
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://fr.indeed.com/")
    verify_you_are_human(driver)
    click_verification(driver)
    
    driver.quit()