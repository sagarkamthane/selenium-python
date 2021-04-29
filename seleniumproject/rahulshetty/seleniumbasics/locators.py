from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("sagar.txt kamthane")
#driver.find_element(By.NAME, "name").send_keys("sagar.txt kamthane")
def enter_name(user_name):
    name = driver.find_element(By.NAME, "name").send_keys(user_name)
    return name
enter_name('sagar')

driver.find_element_by_id("exampleCheck1").click()

driver.find_element_by_css_selector("input[name = 'email']").send_keys("sk@gmail.com")   #css selector

driver.find_element_by_xpath("//input[@type = 'submit']").click() #X-path

print(driver.find_element_by_class_name('alert-success').text)
print(driver.find_element_by_css_selector("div[class *= 'alert-success']").text)   #css regural expression , selects provided value from set of values , tag name is compulsory
print(driver.find_element_by_xpath("//div[contains(@class, 'alert-success')]").text)     #Xpath regural expression , selects provided value from set of values, tag name not compulsory

