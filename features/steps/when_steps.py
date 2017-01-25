from behave import when


""" Click """
@when("Click by Id {Id}")
def step_impl(context, Id):
    context.page.click_id(Id)

@when("Click by Name {name}")
def step_impl(context, name):
    context.page.click_name(name)

@when("Click by Xpath {xpath}")
def step_impl(context, xpath):
    context.page.click_xpath(xpath)

@when("Click by Link Text {text}")
def step_impl(context, text):
    context.page.click_link_text(text)

@when("Click by Partial Link Text {partial}")
def step_impl(context, partial):
    context.page.click_partial_link_text(partial)

@when("Click by Tag Name {tag}")
def step_impl(context, tag):
    context.page.click_tag_name(tag)

@when("Click by Tag Text {tag} with {text}")
def step_impl(context, tag, text):
    context.page.click_tag_text(tag, text)

@when("Click by Class {name}")
def step_impl(context, name):
    context.page.click_class_name(name)

@when("Click by Css {css}")
def step_impl(context, css):
    context.page.click_css(css)

@when("Click button with name {name}")
def step_impl(context, name):
    context.page.click_button_name(name)


""" Fill """
@when("Fill field by ID {fieldID} with {value}")
def step_impl(context, fieldID, value):
    context.page.fill_id(fieldID, value)
    #context.page.login_as(email, password)

@when("Fill field by Name {name} with {value}")
def step_impl(context, name, value):
    context.page.fill_name(name, value)

@when("Fill field by Xpath {xpath} with {value}")
def step_impl(context, xpath, value):
    context.page.fill_xpath(xpath, value)

@when("Fill field by Class name {name} with {value}")
def step_impl(context, name, value):
    context.page.fill_class_name(name, value)

@when("Fill field by Css {css} with {value}")
def step_impl(context, css, value):
    context.page.fill_css(css, value)


""" Wait """
@when("Wait {seconds} seconds")
def step_impl(context, seconds):
    context.page.wait(seconds)

@when("I wait {seconds} seconds until see text {text}")
def step_impl(context, seconds, text):
    context.page.wait_until_text(seconds, text)

