from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.instagram.com/accounts/login/")

time.sleep(1)

username_input = driver.find_element_by_name("username")
username_input.clear()
username_input.send_keys("volkantolu")

password_input = driver.find_element_by_name("password")
password_input.clear()
password_input.send_keys("12345678")

login_button = driver.find_element_by_xpath("//*[@type='submit']")
login_button.click()

time.sleep(1)

driver.close()
