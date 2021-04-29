import time

import selenium
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(7)
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
driver.find_element_by_class_name("search-button").click()

count = driver.find_elements_by_xpath("//div[@class='products']/div")

print(len(count))

buttons = driver.find_elements_by_xpath("//div[@class='product-action']")

for button in buttons :
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//div[@class='action-block']/button").click()
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
print(driver.find_element_by_class_name("promoInfo").text)
driver.find_element_by_xpath("div[class='products']/div/button").click()


