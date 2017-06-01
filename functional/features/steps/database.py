from behave import *
from django.core.management import call_command


@given('there are registered runners')
def impl(context):
    call_command('loaddata', 'initial_data')
