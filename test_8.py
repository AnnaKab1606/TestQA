import datetime
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
base_url = 'https://demoqa.com/radio-buttons'
driver.get(base_url)
driver.maximize_window()

# check_box = driver.find_element(By.XPATH,"//button[@aria-label='Toggle']")
# check_box.click()

radio_button = driver.find_element(By.XPATH,"//label[@for='yesRadio']")
radio_button.click()




time.sleep(5)
driver.quit()