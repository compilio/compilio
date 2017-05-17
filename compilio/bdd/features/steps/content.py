from behave import *


@given('I take a screenshot')
def impl(context):
    context.browser.save_screenshot('screenshot.png')


@then('I should see "{text}"')
def impl(context, text):
    assert text in context.browser.page_source, \
        "Cannot find %r in page" % text


@then('the page\'s title should be "{title}"')
def impl(context, title):
    page_title = context.browser.find_element_by_css_selector('h2:first-of-type').text
    assert title == page_title, \
        "\"%r\" is different from the page\'s title \"%r\"" % (title, page_title)
