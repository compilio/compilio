from behave import *
from selenium import webdriver
from django.core import management


def before_all(context):
    context.browser = webdriver.Chrome()


def before_scenario(context, scenario):
    management.call_command('flush', verbosity=0, interactive=False)


def after_all(context):
    context.browser.quit()
    context.browser = None
