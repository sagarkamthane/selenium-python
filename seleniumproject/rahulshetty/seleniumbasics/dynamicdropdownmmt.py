from selenium import webdriver
import time
from selenium.webdriver.support import select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")
driver.get("https://www.makemytrip.com/")

driver.find_elements_by_id("fromCity").click()
driver.find_element_by_class_name("react-autosuggest__input").send_keys("mum")
driver.find_elements_by_css_selector("//li[@class = 'react-autosuggest__suggestion']/div/div[2]")

