from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")

driver.get("https://the-internet.herokuapp.com/iframe")

#frame . iFrame, frameset
driver.switch_to.frame("mce_0_ifr") #frame id or frame name or index value

driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Hello world!")

driver.switch_to.default_content()
assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element_by_tag_name("h3").text