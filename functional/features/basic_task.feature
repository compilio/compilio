Feature: Basic tasks

  As a Compilio anonymous user,
  I want to be able to start basic compilation tasks on Compilio.

  Scenario: Start a cat task from the homepage
    Given I am on the / page
    And I wait for 2 seconds
    And I drop file image.png into input drop-area
    And I click on id_cat
