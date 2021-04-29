import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements_by_xpath("//input[@type = 'checkbox']")
print(len(checkboxes))

# for checkbox in checkboxes:
#     checkbox.click()
#     assert checkbox.is_selected()

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()


