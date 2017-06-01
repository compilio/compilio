Feature: Basic tasks

  As a Compilio anonymous user,
  I want to be able to start basic compilation tasks on Compilio.

  Background:
    Given there are registered runners

  Scenario: I should see the compilers list
    Given I am on the / page
    Then I should see "List files"

  Scenario: Start a cat task from the homepage
    Given I am on the / page
    And I drop file image.png into input drop-area
    And I click on cat
    And I wait for 2 seconds
    Then I should see "This task was a List contents compilation launched now."
    And I should see "This task is not linked to your account."
    Given I wait for 5 seconds
    Then I should see "success"

  Scenario: Start a cat task as a registered user
    Given user michel exists
    And I am on the /user/login page
    And I fill id_username field with michel
    And I fill id_password field with password
    And I click on id_submit
    And I go to the / page
    And I drop file image.png into input drop-area
    And I click on cat
    And I wait for 2 seconds
    Then I should see "This task was a List contents compilation launched now."
    And I should see "This task has been saved to your account."
    Given I wait for 5 seconds
    Then I should see "success"

  Scenario: Listing tasks
    Given I am on the / page
    And I drop file image.png into input drop-area
    And I click on cat
    And I wait for 3 seconds
    And I go to the /tasks page
    Then I should see "Listing files"
