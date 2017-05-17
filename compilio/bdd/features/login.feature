Feature: Login

  As a Compilio registered user,
  I want to be able to connect to my account.

  Background:
    Given user michel exists

  Scenario: Connect to my account using right credentials
    Given I am on the /user/login page
    And I fill id_username field with michel
    And I fill id_password field with password
    And I click on id_submit
    Then I should be on the /tasks page
    And I should see "Hello michel!"

  Scenario: Connect to my account using wrong credentials
    Given I am on the /user/login page
    And I fill id_username field with michel
    And I fill id_password field with wrong password
    And I click on id_submit
    Then I should be on the /user/login page
    And I should see "Please enter a correct username and password."
