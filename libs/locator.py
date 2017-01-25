from selenium.webdriver.common.by import By

class Locator(object):
    @staticmethod
    def byId(element):
        return (By.ID, element)

    @staticmethod
    def byName(element):
        return (By.NAME, element)

    @staticmethod
    def byXPath(element):
        return (By.XPATH, element)

    @staticmethod
    def byLinkText(element):
        return (By.LINK_TEXT, element)

    @staticmethod
    def byPartialLinkText(element):
        return (By.PARTIAL_LINK_TEXT, element)

    @staticmethod
    def byTagName(element):
        return (By.TAG_NAME, element)

    @staticmethod
    def byClassName(element):
        return (By.CLASS_NAME, element)

    @staticmethod
    def byCssSelector(element):
        return (By.CSS_SELECTOR, element)