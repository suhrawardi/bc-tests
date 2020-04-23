from datetime import datetime
import logging
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


logger = logging.getLogger('Browser')


class Chromium():

    def __init__(self):
        self.timeout = 15
        chrome_options = self.__options()
        capabilities = self.__capabilities()
        logger.debug('Instantiated a new Chrome instance')
        self.instance = webdriver.Chrome(chrome_options=chrome_options,
                                         desired_capabilities=capabilities)
        self.wait = WebDriverWait(self.instance, self.timeout)

    def fill_in(self, key, value):
        self.find_input(key).send_keys(value)

    def find_input(self, key):
        label_xpath = "//label[contains(.,'" + key + "')]/following::input[1]"
        aria_label_xpath = "//input[contains(@aria-label,'" + key + "')][1]"
        xpath = label_xpath + ' | ' + aria_label_xpath
        return self.find_element_by_xpath(xpath)

    def click_on_button(self, value):
        self.__click("//button[contains(.,'" + value + "')]")

    def follow_the_link(self, value):
        self.__click("//a[contains(.,'" + value + "')]")

    def follow_the_navigation_item(self, value):
        navbar = "//div[contains(@class,'nav-bar-content')]"
        span = "//span[@aria-label='" + value + "']"
        self.__click(navbar + span + "[contains(.,'" + value + "')]")

    def select(self, key, value):
        xpath = "[contains(@aria-label,'" + key + "')][1]"
        self.__click("//span[@role='textbox']" + xpath)
        time.sleep(2)
        select = Select(self.find_element_by_xpath("//select" + xpath))
        select.select_by_visible_text(value)

    def switch_to_iframe(self):
        self.wait.until(lambda x: x.find_element_by_tag_name('iframe'))
        iframe = self.find_element_by_tag_name('iframe')
        self.instance.switch_to_frame(iframe)

    def wait_until_form_exists(self, text):
        form_xpath = "//form[contains(@class,'document')]"
        xpath = form_xpath + "//*[contains(.,'" + text + "')]"
        self.wait_until_element_exists(xpath)

    def wait_until_element_exists(self, xpath):
        try:
            self.wait.until(lambda x: x.find_element_by_xpath(xpath))
        except TimeoutException:
            self.save_screenshot('expected_element_not_found')
            raise TimeoutException('Expected page to contain: ' + xpath)

    def wait_until_page_contains(self, text):
        xpath = "//*[contains(normalize-space(.),'" + text + "')]"
        condition = lambda x: x.find_element_by_xpath(xpath).is_displayed()
        try:
            self.wait.until(condition)
        except TimeoutException:
            self.save_screenshot('expected_text_not_found')
            logger.info('Not found: ' + xpath)
            raise TimeoutException('Expected page to contain text: ' + text)

    def save_screenshot(self, name):
        prefix = datetime.now().strftime('%Y%m%d-%H%M%S.%f')
        underscored = name.replace(' ', '_')
        path = 'reports/screenshots/' + prefix + '_' + underscored + '.png'
        self.instance.save_screenshot(path)
        logger.info('Saved screenshot %s from %s', path, self.current_url)

    def dump(self):
        for entry in self.instance.get_log('browser'):
            logger.info(entry)

    def shutdown(self):
        self.instance.quit()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __click(self, xpath):
        try:
            self.find_element_by_xpath(xpath).click()
        except NoSuchElementException:
            raise NoSuchElementException('Element not found: ' + xpath)

    def __capabilities(self):
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['acceptSslCerts'] = True
        capabilities['acceptInsecureCerts'] = True
        capabilities['loggingPrefs'] = {'browser': 'ALL'}
        return capabilities

    def __options(self):
        chrome_options = webdriver.ChromeOptions()
        if os.getenv('DEBUG') != 'True':
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        return chrome_options
