from behave import *
import os


@given('I fill {field} field with {data}')
def impl(context, field, data):
    context.browser.find_element_by_id(field).send_keys(data)


@given('I drop file {file} into input {field}')
def impl(context, file, field):
    context.browser.find_element_by_id(field).send_keys(os.getcwd() + "/fixtures/" + "fake_file.txt")
