from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def on_click_fields(self, key_field, value_field):
    driver = self.driver
    userName = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, key_field)))
    userName.send_keys(value_field)

def open_login_pop_up(self):
    driver = self.driver
    elemJumpin = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "jump-in-btn")))
    elemJumpin.click()
    driver.implicitly_wait(10)

def go_to_team_responses(self, class_name):
    driver = self.driver
    teamResponse = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
    teamResponse.click()
    assessment = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'Capability Maturity Model v3')))
    assessment.click()
    time.sleep(10)