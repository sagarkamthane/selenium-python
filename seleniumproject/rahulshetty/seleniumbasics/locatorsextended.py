import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")
driver.get("https://login.salesforce.com/?locale=in")
#css selector by id
# tagname#id -> tagname optional
driver.find_element_by_css_selector("#username").send_keys("sagar.txt")
driver.find_element_by_css_selector("input#username").send_keys(" kamthane")

#css selector by class name
# tagname.class -> tagname optional
driver.find_element_by_css_selector("input.password").send_keys("Pass")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_css_selector(".password").send_keys("@1234")

#link_text
driver.find_element_by_link_text("Forgot Your Password?").click()  #case sensetive

time.sleep(5)
#creating x-path based upon text
#//tagname[text()='xyz']
driver.find_element_by_xpath("//a[text()='Cancel']").click()

#creating x-path and css by traversing tags
#x-path ParentTag ChildTag
print(driver.find_element_by_xpath("//form[@name = 'login']/div[1]/label").text) # o/p = username
print(driver.find_element_by_xpath("//form[@name = 'login']/label[1]").text) #o/p = passsword

#css parentTag childTag
print(driver.find_element_by_css_selector("form[name = 'login'] label:nth-child(4)").text) #o/p = passsword



