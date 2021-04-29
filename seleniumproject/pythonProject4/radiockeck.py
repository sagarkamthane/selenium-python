import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

options = driver.find_elements_by_xpath("//input[@type='checkbox']")

time.sleep(2)
for checkbox in options:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()


radios = driver.find_elements_by_class_name("radioButton")

radios[1].click()
radios[2].is_selected()