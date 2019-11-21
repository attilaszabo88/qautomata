from selenium.webdriver.common.by import By

from scenarios.scenario import Scenario


class TestLoginScenario(Scenario):
    def test_login(self):
        self.login(
            hostname='https://staging-app.amplicare.com/login',
            user='demo@amplicare.com',
            password='AMPLId3mo',
        )

        random_element = self.driver.find_element(
            By.LINK_TEXT, "Recently Viewed Patients"
        )
        self.assertEqual(random_element.text, "Recently Viewed Patients")

    def test_logout(self):
        self.login(
            hostname='https://staging-app.amplicare.com/login',
            user='demo@amplicare.com',
            password='AMPLId3mo',
        )

        self.logout()
