import time
import selenium
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


driver.find_element_by_id("name").send_keys("option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)

assert "option3" in alert.text
alert.dismiss()

