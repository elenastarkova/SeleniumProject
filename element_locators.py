from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#initializing chrome driver
driver = webdriver.Chrome()

#test scenarion starts here
driver.get("http://automationpractice.com")
time.sleep(5)

search_box=driver.find_element_by_name("search_query")
search_box.send_keys('dress')
#driver.find_element_by_xpath('//button[@name="submit_search"]').click()
search_box=driver.find_element_by_css_selector('button.button_search"]').click()
#driver.find_element(By.PARTIAL_LINKTEXT)
time.sleep(5)

driver.find_element_by_partial_link_text('Sign in').click()