import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")

list1 = []
list2 = []

driver.implicitly_wait(5)
#waits for 5 sec if object is not displayed
#Global wait
#if object loads in 1 sec then doesn't wait till 5 sec
#if object doesn't load till 5 sec, max wait is of 5 sec

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(5)
veggies = driver.find_elements_by_xpath("//div[@class = 'products']/div")
print(len(veggies))
assert len(veggies) > 0

cart = driver.find_elements_by_xpath("//div[@class='product-action']/button")
#//div[@class='product-action']/button/parent::div/parent::div/h4
for good in cart:
    list1.append(good.find_element_by_xpath("parent::div/parent::div/h4").text)   #/parent::tagname
    good.click()

driver.find_element_by_css_selector("img[alt = 'Cart']").click()
driver.find_element_by_xpath("//button[text() = 'PROCEED TO CHECKOUT']").click()

veggies = driver.find_elements_by_css_selector("p[class = 'product-name']")

for veg in veggies:
    list2.append(veg.text)

print(list1)
print(list2)

assert list1 == list2[:3]


