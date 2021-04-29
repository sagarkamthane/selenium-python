from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

driver.switch_to.window(driver.window_handles[1])   #(parentwindow, child window) = [0,1]
assert "New Window" == driver.find_element_by_xpath("//h3[text()='New Window']").text
driver.close()

driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
