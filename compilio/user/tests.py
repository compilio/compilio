from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()


def test_register(self):
    selenium = self.selenium

    selenium.get('http://127.0.0.1:8000/user/register')

    username = selenium.find_element_by_id('id_username')
    email = selenium.find_element_by_id('id_email')
    password1 = selenium.find_element_by_id('id_password1')
    password2 = selenium.find_element_by_id('id_password2')

    submit = selenium.find_element_by_name('register')

    username.send_keys('Michel')
    email.send_keys('michel@example.com')
    password1.send_keys('m1chelPWD')
    password2.send_keys('m1chelPWD')

    submit.send_keys(Keys.RETURN)

    assert 'Login to Compilio' in selenium.title
