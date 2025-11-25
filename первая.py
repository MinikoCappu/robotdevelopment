'''from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

driver.get("https://www.istu.edu")
button = driver.find_element(by = By.CLASS_NAME, value = "left")
button.click()
'''
from selenium.webdriver.edge.options import Options
from selenium import webdriver
options = Options()
options.binary_location = "/usr/bin/microsoft-edge"
driver = webdriver.Edge(options = options)
driver.get("https://www.istu.edu")
print(driver.title)
driver.quit()