from selenium import webdriver
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Safari()
driver.get("https://www.youtube.com")
driver.maximize_window()
driver.get("https://www.youtube.com/feed/subscriptions")
driver.minimize_window()
driver.back()
driver.refresh()
print(driver.current_url)
driver.close()




