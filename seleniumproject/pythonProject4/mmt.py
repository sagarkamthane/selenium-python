import time
import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://www.makemytrip.com/")

#driver.refresh()
time.sleep(5)

#from city
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("kol")

time.sleep(2)

cities = driver.find_elements_by_xpath("//li[@role='option']/div/div[1]/p[1]")

print(len(cities))

for city in cities :
    if city.text == "Kolda, Senegal" :
        city.click()
        break

time.sleep(5)
#To city
#driver.find_element_by_id("toCity").click()

time.sleep(2)

driver.find_element_by_css_selector("input[placeholder='To']").send_keys("abu D")
cities2 = driver.find_elements_by_xpath("//li[@role='option']/div/div[1]/p[2]")
print(cities2)
for city2 in cities2:
    time.sleep(2)
    if city2.text == "Yas Island Seaplane Base" :
        city2.click()
        break

time.sleep(2)

days = driver.find_elements_by_xpath("//div[@class='DayPicker-Months']/div[0]/div/div/div/p")

for day in days:
    if day.get_attribute("value") == "30" :
        day.click()
        assert day == "30" 







