import os

#from xvfbwrapper import Xvfb

from libs.config import base_url, driver_default, xvfb_use, xvfb_width, xvfb_height
from libs.utils import capture, file_path
from libs.browsers import Browsers
from libs.page import Page


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


# Runs before each Given, When and Then step.
def before_step(context, step):
    pass


# Runs after each step
def after_step(context, step):
    #session.clear_cookies_if_required(session.Stage.step, context)
    if step.status == "failed":
        capture(context, step.name)
        #print("step failed")
    #if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
    #    import ipdb
    #    ipdb.post_mortem(step.exc_traceback)


# Runs before each full scenario (complete Given, When, Then definition)
def before_scenario(context, scenario):
    pass

# Runs after each scenario
def after_scenario(context, scenario):
    #session.clear_cookies_if_required(session.Stage.scenario, context)
    #if scenario.status == "failed":
    #    screenshot.capture_failure(context, scenario)
    capture(context, scenario.name)
    pass

# Runs before each feature file
def before_feature(context, feature):
    context.driver = Browsers.get(driver_default)
    context.page = Page(context.driver)
    pass

# Runs after each feature
def after_feature(context, feature):
    #session.clear_cookies_if_required(session.Stage.feature, context)
    context.driver.quit()
    pass

def before_all(context):
    #browsertype = configuration.get_browser()
    #context.driver = driver.switch_browser(browsertype)

    #if xvfb_use:
    #    context.display = Xvfb(width=xvfb_width, height=xvfb_height)
    #    context.display.start()

    setup_debug_on_error(context.config.userdata)
    context.base_url = base_url
    context.base_dir = os.getcwd()

def after_all(context):
    #session.clear_cookies_if_required(session.Stage.lifetime, context)
    # Very last thing to run.
    #if xvfb_use:
    #    context.display.stop()
    pass
