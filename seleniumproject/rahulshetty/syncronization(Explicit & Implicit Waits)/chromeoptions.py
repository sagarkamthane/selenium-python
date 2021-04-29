from selenium import webdriver
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver", options = options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)


driver.close()