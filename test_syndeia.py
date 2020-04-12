import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

main_url = 'http://storeman1.intercax.com:9000'
# Firefox driver
# driver = webdriver.Firefox(
#       executable_path='C:\\geckodriver\\geckodriver.exe')

# Edge driver
# driver = webdriver.Edge('C:\\edgedriver_win64\\msedgedriver.exe')

# Chrome driver
driver = webdriver.Chrome('C:\\chromedriver_win32\\chromedriver.exe')

def login():
  driver.get(main_url)

  username = driver.find_element_by_id('username')
  username.send_keys('super.user')

  password = driver.find_element_by_id('password')
  password.send_keys('syn45ia')

  submit_button = driver.find_element_by_tag_name('button')
  submit_button.send_keys(Keys.RETURN)

  # driver.implicitly_wait(30)

  assert "No results found" not in driver.page_source
  # user()

def user():
  driver.get('http://storeman1.intercax.com:9000/user-management')

  # findUser = driver.find_element_by_link_text('nitin.reddy@intercax.com')
  # findUser.send_keys(Keys.RETURN)


login()
# user()
# driver.close()
