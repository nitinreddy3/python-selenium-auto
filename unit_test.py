import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\\geckodriver\\geckodriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://localhost:9000/")
        self.assertIn("Telstra Software Engineering Capability Assessment Tool", driver.title)

        # Code to open modal pop up
        self.open_login_pop_up()

        # Code to fill in user name and password
        self.on_click_fields("login-username", "guest")
        self.on_click_fields("login-password", "password")

        # Submit after details are filled
        driver.find_element(By.XPATH, '//button[contains(text(), "Go")]').click()

        module_list = ["teams", "all-assessments", "my-assessments", "permission-metrix", "team-responses", "configure-assessments",
            "team-profiles", "team-profile", "hpse-metrics", "metrics-onboarding", "health-metrics"]

        self.go_to_team_responses("team-responses")
        self.go_to_team_responses("team-profiles")
        self.go_to_team_responses("hpse-metrics")
        self.go_to_team_responses("health-metrics")

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
        time.sleep(20)

if __name__ == "__main__":
    unittest.main()