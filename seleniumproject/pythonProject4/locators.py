import time
from select import select
from selenium import common

import selenium
from selenium.webdriver.support.select import Select

selenium.webdriver.support.select.Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/#")
driver.maximize_window()
driver.refresh()

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")
print(len(countries))

for country in countries:
    if country.text == "India" :
        country.click()
        break


assert driver.find_element_by_id("autosuggest").get_attribute("value") == "India"






#driver.find_element_by_name("q").send_keys("rahulshetty angularpractice")
#driver.find_element_by_css_selector("input[maxlength='2048']").send_keys("rahul shetty angular practice")
#driver.find_element_by_xpath("//input[@aria-label='Search']").send_keys("rahul shetty angular practice")
#driver.find_element_by_name("btnK").submit()
#print(driver.find_element_by_xpath("//*[@id='result-stats']").text)
#print(driver.find_element_by_id("result-stats").text)

#driver.find_element_by_css_selector("[aria-label='Menu']").click()
#driver.find_element_by_xpath("//input[@id='username']").send_keys("csfphase@gmail.com")
#driver.find_element_by_id("password").send_keys("csfphase2@vuclip")
#driver.find_element_by_id("password").clear()
#driver.find_element_by_css_selector("form[name='login'] label").send_keys(1234) #css traverse
#driver.find_element_by_xpath("//div[@class='w0 pr ln3 p16 remember']/input").click() #xpath traverse
#driver.find_element_by_id("Login").click()
#driver.refresh()
#driver.find_element_by_link_text("Forgot Your Password?").click()
#driver.find_element_by_xpath("//a[text()='Cancel']").click()
#driver.close()

#dropdown
#dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Male")
#dropdown.select_by_index("1")

#print(driver.find_element_by_xpath("//label[@for='username']").text)
#print(driver.find_elements_by_xpath("//form[@name='login']/label").text)
#driver.close()

