from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Scenario(TestCase):
    """
    Basic scenario class.
    """

    driver = None
    DEFAULT_SCREEN_WIDTH = 1920
    DEFAULT_SCREEN_HEIGHT = 1080

    def setup_method(self, method):
        self.driver = webdriver.Chrome()

    def teardown_method(self, method):
        self.driver.quit()

    def login(self, hostname, user, password):
        self.driver.get(hostname)
        self.driver.set_window_size(self.DEFAULT_SCREEN_WIDTH, self.DEFAULT_SCREEN_HEIGHT)
        self.driver.find_element(By.ID, "identification").click()
        self.driver.find_element(By.ID, "identification").send_keys(user)
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "authenticate").click()
        self.driver.implicitly_wait(15)

    def logout(self):
        action = ActionChains(self.driver)
        settings = self.driver.find_element(By.LINK_TEXT, "Settings")
        action.move_to_element(settings).perform()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.driver.implicitly_wait(15)

    def go_to_patients(self):
        self.driver.find_element(By.LINK_TEXT, 'Patients').click()
        self.driver.implicitly_wait(15)

