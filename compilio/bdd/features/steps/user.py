from behave import *
from django.contrib.auth.models import User


@then('user {username} should exists')
def impl(context, username):
    User.objects.filter(username=username).exists()
