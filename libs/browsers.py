from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

from libs.config import driver_default

class Browsers(object):
    browsers = {
        "chrome": ["Chrome", "chromedriver"],
        "firefox": ["Firefox", "geckodriver"],
        "ie": ["IE", "Internet Explorer"],
        "phantom": ["PH", "Phantom"]
    }

    @classmethod
    def get(self, browser):
        return eval("webdriver." + self.browsers[browser][0] + "()")
