import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("a[href *= 'shop']").click()

#driver.find_element_by_xpath("//a[text() = 'Blackberry']/parent::h4/parent::div[1]//parent::div[1]/div[2]/button").click()

#or
#products = driver.find_elements_by_class_name("card h-100") #This doesn't work
products = driver.find_elements_by_xpath("//div[@class = 'card h-100']")

for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    if product.find_element_by_xpath("div/h4/a").text == "Blackberry":
        product.find_element_by_xpath("div[2]/button").click() #div will also work as there is no button child in div[1]
        break

driver.find_element_by_css_selector("a[class *= 'btn-primary']").click()


if driver.find_element_by_xpath("//h4[@class = 'media-heading']/a").text == "Blackberry" :
    driver.find_element_by_css_selector(".btn-success").click()

#driver.implicitly_wait(10)
driver.find_element_by_css_selector(".validate").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element_by_xpath("//a[text() = 'India']").click()
driver.find_element_by_css_selector("label[for = 'checkbox2']").click()
#time.sleep(5)
#wait.until(expected_conditions.element_located_to_be_selected((By.ID, 'checkbox2')))
print(driver.find_element_by_css_selector("input[id = 'checkbox2']").is_selected())
driver.find_element_by_css_selector(".btn-success").click()

assert "Success" in driver.find_element_by_css_selector(".alert").text



