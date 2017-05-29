import time
from behave import *
from selenium.common.exceptions import NoSuchElementException


@given('I am on the homepage')
def impl(context):
    context.browser.get(context.config.server_url)


@given('I am on the {page} page')
@given('I go to the {page} page')
def impl(context, page):
    context.browser.get(context.config.server_url + page)


@given('I click on {target}')
def impl(context, target):
    try:
        element = context.browser.find_element_by_id(target)
    except NoSuchElementException:
        element = context.browser.find_element_by_link_text(target)

    element.click()


@then('I should be on the {page} page')
def impl(context, page):
    assert context.config.server_url + page in context.browser.current_url, \
        "%r does not match %r" % (context.config.server_url + page, context.browser.current_url)


@given('I wait for {wait} seconds')
def impl(context, wait):
    time.sleep(int(wait))
