
class Saucelabs(object):
  @staticmethod
  def getInstance(webdriver, user, key, desired_cap):
    return webdriver.Remote(
       command_executor='http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (user, key),
       desired_capabilities=desired_cap)


class Firefox(object):
  @staticmethod
  def getInstance(webdriver):
    return webdriver.Firefox()

class Chrome(object):
  @staticmethod
  def getInstance(webdriver):
    return webdriver.Chrome('drivers/chromedriver')

