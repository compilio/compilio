from selenium import webdriver
from django.core import management
from pyvirtualdisplay import Display
import os


def before_all(context):
    if 'TRAVIS' in os.environ:
        context.display = Display(visible=0, size=(1024, 768))
        context.display.start()

    context.browser = webdriver.Chrome()


def before_scenario(context, scenario):
    management.call_command('flush', verbosity=0, interactive=False)


def after_all(context):
    context.browser.quit()
    context.browser = None
    if 'TRAVIS' in os.environ:
        context.display.stop()
