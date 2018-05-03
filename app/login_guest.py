import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utility.common_methods import on_click_fields, open_login_pop_up, go_to_team_responses


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
        on_click_fields(self, "login-username", "guest")
        on_click_fields(self, "login-password", "password")

        # Submit after details are filled
        driver.find_element(By.XPATH, '//button[contains(text(), "Go")]').click()

        if driver.find_element_by_partial_link_text('Guest').is_displayed:
            go_to_team_responses(self, "team-responses")
            go_to_team_responses(self, "team-profiles")
            go_to_team_responses(self, "hpse-metrics")
            go_to_team_responses(self, "health-metrics")


if __name__ == "__main__":
    unittest.main()
