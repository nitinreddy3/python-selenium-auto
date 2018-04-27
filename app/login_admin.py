import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.common_methods import open_login_pop_up, on_click_fields, go_to_team_responses

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\\geckodriver\\geckodriver.exe')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://localhost:9000/")
        self.assertIn("Telstra Software Engineering Capability Assessment Tool", driver.title)

        # Code to open modal pop up
        open_login_pop_up(self)

        # Code to fill in user name and password
        on_click_fields(self, "login-username", "admin")
        on_click_fields(self, "login-password", "cmmAdmin#1")

        # Submit after details are filled
        driver.find_element(By.XPATH, '//button[contains(text(), "Go")]').click()

        if driver.find_element_by_partial_link_text('Admin').is_displayed:
            go_to_team_responses(self, "all-assessments")
            go_to_team_responses(self, "teams")
            go_to_team_responses(self, "permission-metrix")
            go_to_team_responses(self, "team-responses")
            go_to_team_responses(self, "configure-assessments")
            go_to_team_responses(self, "team-profiles")
            go_to_team_responses(self, "hpse-metrics")
            go_to_team_responses(self, "metrics-onboarding")
            go_to_team_responses(self, "health-metrics")

if __name__ == "__main__":
    unittest.main()