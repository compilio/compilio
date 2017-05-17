Feature: Navigating

  As a Compilio user,
  I should be able to navigate through pages.

  Background:
    Given I am on the homepage

  Scenario: Going to the compilation section
    Given I click on Compile
    Then the page's title should be "Start compiling"
    And I should be on the / page

  Scenario: Going the the tasks section
    Given I click on My tasks
    Then the page's title should be "My tasks"
    And I should be on the /tasks page

  Scenario: Going to the documentation section
    Given I click on Documentation
    Then the page's title should be "Documentation"
    And I should be on the /doc page
