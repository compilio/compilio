from behave import *
import os
import functional


@given('I fill {field} field with {data}')
def impl(context, field, data):
    context.browser.find_element_by_id(field).send_keys(data)


@given('I drop file {file} into input {field}')
def impl(context, file, field):
    context.browser.find_element_by_id(field).send_keys(
        os.path.dirname(functional.__path__[0] + "/features/fixtures/") + "/fake_file.txt"
    )
