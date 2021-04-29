import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index("1")

driver.find_element_by_class_name("btn-success").click()
message = driver.find_element_by_class_name("alert-success").text
print(message)
assert "success" in message

#driver.close()

