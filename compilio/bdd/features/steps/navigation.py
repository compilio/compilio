from behave import *


@given('I go to {page} page')
def impl(context, page):
    context.browser.get(context.config.server_url + page)


@given('I fill {field} field with {data}')
def impl(context, field, data):
    context.browser.find_element_by_id(field).send_keys(data)


@given('I click on {field}')
def impl(context, field):
    context.browser.find_element_by_id(field).click()
    context.browser.implicitly_wait(5)


@given('I take a screenshot')
def impl(context):
    context.browser.save_screenshot('screenshot.png')


@then('I should be on {page} page')
def impl(context, page):
    assert context.config.server_url + page in context.browser.current_url, \
        "%r does not match %r" % (context.config.server_url + page, context.browser.current_url)
