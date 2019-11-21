from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By


class Scenario(TestCase):
    """
    Basic scenario class.
    """

    driver = None

    def setup_method(self, method):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def login(self, hostname, user, password):
        self.driver.get(hostname)
        self.driver.set_window_size(1200, 800)
        self.driver.find_element(By.ID, "identification").click()
        self.driver.find_element(By.ID, "identification").send_keys(user)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "authenticate").click()
        self.driver.implicitly_wait(15)

    def logout(self):
        pass
