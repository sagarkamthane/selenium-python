import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait #for explicit wait
from selenium.webdriver.support import expected_conditions #for explicit wait
from selenium.webdriver.common.by import By #for explicit wait

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/seleniumPractise/")


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

for good in cart:
    good.click()

driver.find_element_by_css_selector("img[alt = 'Cart']").click()
driver.find_element_by_xpath("//button[text() = 'PROCEED TO CHECKOUT']").click()


wait = WebDriverWait(driver, 10)  #driver, 5 sec
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("button.promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
successtext = driver.find_element_by_css_selector(".promoInfo").text

assert successtext == "Code applied ..!"
