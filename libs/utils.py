import os

from slugify import slugify


def capture(context, name):
    return context.driver.get_screenshot_as_file(context.base_dir + "/screenshots/" + slugify(name) + '.png')

def file_path(file_name):
    return os.getcwd() + "./resources/" + file_name

