from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/sagarkamthane/Downloads/chromedriver")
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
driver.back()
driver.refresh()
driver.quit()
