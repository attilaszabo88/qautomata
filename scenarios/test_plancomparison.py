from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from scenarios.scenario import Scenario


class TestPlanComparisonScenario(Scenario):
    def test_plan_comparison(self):
        self.login(
            hostname='https://staging-app.amplicare.com/login',
            user='demo@amplicare.com',
            password='AMPLId3mo',
        )
        self.go_to_patients_page()
        self.driver.find_elements_by_xpath("//*[contains(@id, 'patient-')]")[2].click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.CSS_SELECTOR, '.mainTabs .mainTabs-item:nth-child(3)').click()
        plan1 = self.driver.find_element(By.CSS_SELECTOR, ".plan:nth-of-type(3) .checker").find_element_by_xpath("..")
        plan1.location_once_scrolled_into_view
        plan1.click()
        plan2 = self.driver.find_element(By.CSS_SELECTOR, ".plan:nth-of-type(4) .checker").find_element_by_xpath("..")
        plan2.location_once_scrolled_into_view
        plan2.click()
        plan3 = self.driver.find_element(By.CSS_SELECTOR, ".plan:nth-of-type(5) .checker").find_element_by_xpath("..")
        plan3.location_once_scrolled_into_view
        plan3.click()
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID, "compare-plans").click()
        self.driver.implicitly_wait(15)
        self.logout()
