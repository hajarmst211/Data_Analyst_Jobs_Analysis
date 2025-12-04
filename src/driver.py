from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4325643765&geoId=105015875&origin=JOBS_HOME_LOCATION_HISTORY"
keyword_search_box_ID = "jobs-search-box-keyword-id-ember99" 
country_search_box_ID = "jobs-search-box-location-id-ember99"

class driver():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def open_driver(self):
        self.driver.get(URL)
        
    def tearDown(self):
        self.driver.close()   

    def search_keyword(self, keyword):
        keyword_search_box = self.driver.find_element(By.ID, keyword_search_box_ID)
        self.driver.implicitly_wait(2)
        keyword_search_box.clear()
        keyword_search_box.send_keys(keyword)
        keyword_search_box.send_keys(Keys.RETURN)

    def search_country(self, country):
        country_search_box = self.driver.find_element(By.ID, country_search_box_ID)
        self.driver.implicitly_wait(2)
        country_search_box.clear()
        country_search_box.send_keys(country)
        country_search_box.send_keys(Keys.RETURN)

    def sing_in(self):
        sign_in_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[1]")
        sign_in_button.click()
    
def main():
    driver = webdriver.Chrome()
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    close_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal__close, .close, button.close"))
    )
    close_btn.click()
'''
    wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, "div.modal__overlay")
    sign_in_button.click()
    
    sign_in_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[1]")
    sign_in_button.click()
    time.sleep(60*60)
    ))
'''

if __name__ == "__main__":
    main()
    
