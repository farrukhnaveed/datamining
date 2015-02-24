import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lettuce import world


logger = logging.getLogger(__name__)


class Helper(object):
    def __init__(self):
        self.driver = world.browser

    def find_xpath_multi_with_text(self, xpath, element_text):
        for element in self.driver.find_elements_by_xpath(xpath):
            if element.text == element_text:
                return element
        return None

    #change---- Added following function
    def find_index_multi_visible_xpath(self, xpath):
        return self.driver.find_elements_by_xpath(xpath)

    def wait_visible_css_selector(self, css_selector):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def wait_visible_xpath(self, xpath):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, xpath)))

    def wait_visible_link(self, link_text):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, link_text)))

    def wait_visible_id(self, element_id):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, element_id)))

    def clickable_path(self, xpath):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.XPATH, xpath)))

    def wait_clickable_id(self, id_name):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.ID, id_name)))

    def wait_present_xpath(self, xpath):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, xpath)))

    def wait_present_id(self, element_id):
        self.wait_action_complete()
        return WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, element_id)))

    def type_text_in_xpath_element(self, element_xpath, some_text):
        my_element = self.wait_visible_xpath(element_xpath)
        my_element.click()
        my_element.clear()
        if some_text != 'Empty':
            my_element.send_keys(some_text)
        # no events are fired when calling clear()
        self.wait_action_complete()

    def type_text_in_id_element(self, id_element, some_text):
        my_element = self.wait_visible_id(id_element)
        my_element.click()
        my_element.clear()
        if some_text != 'Empty':
            my_element.send_keys(some_text)
        self.wait_action_complete()

    def type_text_in_css_element(self, new_description, css_selector):
        description_text = self.wait_visible_css_selector(css_selector)
        description_text.click()
        description_text.clear()
        if new_description != 'Empty':
            description_text.send_keys(new_description)
        self.wait_action_complete()

    def wait_clickable_css_selector(self, css_selector):
        return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    def check_spinner(self):
        return self.driver.find_elements_by_id("loadingImg")

    def wait_action_complete(self):
        if self.check_spinner():
            for i in range(1, 25):
                time.sleep(.2)
                if not self.check_spinner():
                    break
                else:
                    logger.warning("spinner is active")
