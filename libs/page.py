from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from libs.locator import Locator
from libs.utils import file_path

import time

class Page(object):

    def __init__(self, driver):
        self.driver = driver
        #self.driver.implicitly_wait(10)

    def close(self):
        self.driver.quit()

    def wait(self, seconds):
        #self.driver.implicitly_wait(int(seconds))
        time.sleep(int(seconds))

    def wait_until_text(self, seconds, text):
        #self.wait_until_element_clickable(seconds, LoginModalLocators.LNK_MIS_OFERTAS)
        element = WebDriverWait(self.driver, int(seconds)).until(
            EC.text_to_be_present_in_element(Locator.byTagName("h2"), text)
        )

    def title_is(self, text):
        return EC.title_is(text)

    def _webdriver_wait(self, seconds):
        return WebDriverWait(self.driver, float(seconds))

    def wait_until_element_located(self, seconds, element):
        wait = self._webdriver_wait(seconds)
        return wait.until(EC.presence_of_element_located(element))

    def wait_until_element_clickable(self, seconds, element):
        wait = self._webdriver_wait(seconds)
        return wait.until(EC.element_to_be_clickable(element))



    """
    Attach
    """
    def attach_file(self, locator, file_name=''):
        element = self.driver.find_element(*locator)
        element.send_keys(file_path(file_name))
        return element

    def select_value(self, locator, value):
        select = Select(self.driver.find_element(*locator))
        select.select_by_value(value)
        return select

    """
    Click by
    """
    def click(self, locator):
        element = self.driver.find_element(*locator)
        return element.click()

    def click_id(self, Id):
        return self.click(Locator.byId(Id))

    def click_name(self, name):
        return self.click(Locator.byName(name))

    def click_xpath(self, xpath):
        return self.click(Locator.byXPath(xpath))

    def click_link_text(self, text):
        return self.click(Locator.byLinkText(text))

    def click_partial_link_text(self, partial):
        return self.click(Locator.byPartialLinkText(partial))

    def click_tag_name(self, tag):
        return self.click(Locator.byTagName(tag))

    def click_tag_text(self, tag, text):
        return self.click(Locator.byXPath("//%s[contains(.,'%s')]" % (tag, text)))

    def click_class_name(self, name):
        return self.click(Locator.byClassName(name))

    def click_css(self, css):
        return self.click(Locator.byCssSelector(css))


    """
    Fill
    """
    def fill(self, locator, text=''):
        element = self.driver.find_element(*locator)
        return element.send_keys(text)

    def fill_id(self, Id, text=''):
        return self.fill(Locator.byId(Id), text)

    def fill_name(self, name, text=''):
        return self.fill(Locator.byName(name), text)

    def fill_xpath(self, xpath, text=''):
        return self.fill(Locator.byXPath(xpath), text)

    def fill_class_name(self, name, text=''):
        return self.fill(Locator.byClassName(name), text)

    def fill_css(self, css, text=''):
        return self.fill(Locator.byCssSelector(css), text)



    """
    Select
    """
    def select_text(self, locator, text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(text)
        return select

    """
    Clear
    """
    def clear_txt(self,locator):
        a = self.driver.find_element(*locator)
        a.clear()


    def visit(self, path):
        self.driver.visit(path)
        self.current_url = self.driver.current_url

    def verify_url(self, url):
        return self.driver.get_current_url() == url

    def should_have_content(self, content):
        has_content = False
        if self.driver.has_title(content):
            has_content = True
        if self.driver.has_text(content):
            has_content = True
        return has_content


    #def visit(self, location=''):
    #    """
    #    navigate webdriver to different pages
    #    """
    #    url = self.base_url + location
    #    self.driver.get(url)
