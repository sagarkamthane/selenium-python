from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
action.move_to_element(driver.find_element_by_id("mousehover")).perform()
action.move_to_element(driver.find_element_by_link_text("Reload")).click().perform()
action.move_to_element(driver.find_element_by_link_text("Reload").click()).perform()  #this is also valid

driver.maximize_window()
driver.implicitly_wait(5)
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action.context_click(driver.find_element_by_name("download")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()
driver.switch_to.alert.accept()


