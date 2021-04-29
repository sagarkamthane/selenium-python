import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("name").send_keys("sagar.txt")
driver.find_element_by_id("alertbtn").click()

alert1 = driver.switch_to.alert
assert 'sagar.txt' in alert1.text
time.sleep(2)
alert1.accept()

driver.find_element_by_id("name").send_keys("sagar.txt")
driver.find_element_by_id("confirmbtn").click()

alert1 = driver.switch_to.alert
time.sleep(2)
assert 'sagar.txt' in alert1.text
alert1.dismiss()













