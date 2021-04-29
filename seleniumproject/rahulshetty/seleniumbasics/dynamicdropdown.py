import time

from selenium import webdriver


driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
country_id = input("enter a country")
driver.find_element_by_id("autosuggest").send_keys(country_id)

time.sleep(2)

countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
print(countries)
your_country = input("enter your country")
for country in countries:
    if country.text == your_country:
        country.click()
        break

assert driver.find_element_by_id("autosuggest").get_attribute('value') == "india"
