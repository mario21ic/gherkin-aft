from behave import given

""" Load """
@given("Load the Uri {path}")
def step_load_page(context, path):
    context.page.driver.get(context.base_url + path)
