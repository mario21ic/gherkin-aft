from behave import then
from hamcrest import assert_that, equal_to, is_not
from selenium.webdriver.support import expected_conditions as EC


@then("Should redirect to {path}")
def step_impl(context, path):
    assert_that(context.driver.current_url, equal_to(context.base_url + path))

@then("Title is {text}")
def step_impl(context, text):
    assert_that(context.driver.title, equal_to(text))

@then("Title contains {text}")
def step_impl(context, text):
    print(text)
    #print("xD", EC.title_contains(text))
    #return EC.title_contains(text)
