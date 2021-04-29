from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver", options = options)
driver.get("https://www.whirlpoolindia.com/")
driver.refresh()
driver.maximize_window()
elem = driver.find_element(By.PARTIAL_LINK_TEXT, "Support")


logo = driver.find_element(By.XPATH, "//strong[@class = 'logo']/img")
print(logo.location)
print(logo.size)

li =["font-size", "font-weight", "font-stretch", "font-style", "letter-spacing", "text-align", "color", "text-decoration", "font-family" ]
dict1 = {}
dict2 = {}
for i in li:
    dict1[i] = elem.value_of_css_property(i)
    dict2[i] = logo.value_of_css_property(i)

print(dict1, '\n', dict2)


