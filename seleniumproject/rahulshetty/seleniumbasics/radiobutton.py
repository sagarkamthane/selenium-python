import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# radio button
# radio = driver.find_element_by_css_selector("input[value ='radio2']")
# radio.click()
# assert radio.is_selected()

radios = driver.find_elements_by_css_selector("input[type ='radio']")
radios[2].click()
assert radios[2].is_selected()