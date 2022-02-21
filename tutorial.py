from selenium import webdriver

PATH = "/Users/javiercosio/Documents/UPWORD/SELENIUM/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.upword.ai/")
print(driver.title)
driver.quit()