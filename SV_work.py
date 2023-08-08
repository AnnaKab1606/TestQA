from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "https://www.provartesting.com/contact/?utm_source=google&utm_medium=cpc&utm_campaign=uk_competitor&gclid=Cj0KCQjwz8emBhDrARIsANNJjS5nGD0ripp8PE5713StPCS5Ay_rdYqVyo6yxC6-LmVHKhwc618lwqwaAoOeEALw_wcB"
browser = webdriver.Chrome()
browser.get(link)

select = browser.find_element(By.XPATH, '//*[@id="input_11_10"]')
select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value("Romania")

button = browser.find_element(By.XPATH, '//*[@id="input_11_8"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()



# search = browser.find_element(By.XPATH, '//*[@id="ft_search"]/input[1]')
# search.send_keys("Мячик")
# time.sleep(5)
#
# input1 = browser.find_element(By.XPATH,'//*[@id="ft_search"]/div[2]/button/span/svg')
# input1.click()
# time.sleep(3)

# p = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div[2]/div/a/div[1]/h2')
# p = p.text
#
# assert 'Виталий Маклаков. Интервью.' == p
# print('GOOD')



time.sleep(30)
browser.quit()

