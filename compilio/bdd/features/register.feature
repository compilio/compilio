Feature: Register

  As a Compilio anonymous user,
  I want to be able to create my account.

  Scenario: Register on the registration page
    Given I go to /user/register page
    And I fill id_username field with Michel
    And I fill id_email field with michel@example.com
    And I fill id_password1 field with m1chelPWD
    And I fill id_password2 field with m1chelPWD
    And I click on id_submit
    Then user Michel should exists
