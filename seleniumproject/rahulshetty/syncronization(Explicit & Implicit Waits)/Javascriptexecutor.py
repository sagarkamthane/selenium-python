from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("sagar.txt")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))

print(driver.execute_script('return document.getElementsByName("name")[0].value;'))

#click shop button using javascript click

shopButton = driver.find_element_by_link_text("Shop")
driver.execute_script("arguments[0].click();", shopButton)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
