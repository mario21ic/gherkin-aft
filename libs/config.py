import ConfigParser as configparser
import os

def getConfig(section="app", key=""):
    config = configparser.RawConfigParser()
    config.read("config.ini")
    return config.get(section, key)

base_url = getConfig(key="base_url")
driver_default = getConfig("driver", key="default")
#dir_driver = getConfig(key="dir_driver")
#dir_report = getConfig(key="dir_report")
#dir_screenshot = getConfig(key="dir_screenshot")
#dir_resource = getConfig(key="dir_resource")

xvfb_use = getConfig("xvfb", "use")
xvfb_width = getConfig("xvfb", "width")
xvfb_height = getConfig("xvfb", "height")
