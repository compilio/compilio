Feature: RSS feeds

  As a Compilio user,
  I want to be able to follow my tasks using a RSS feed.

  Background:
    Given there are registered runners

  Scenario: Start a cat task as a registered user
    Given user michel exists
    And I am on the /user/login page
    And I fill id_username field with michel
    And I fill id_password field with password
    And I click on id_submit
    And I go to the / page
    And I drop file image.png into input drop-area
    And I click on cat
    And I wait for 3 seconds
    And I go to the /tasks page
    And I click on RSS Feed
    Then I should be on the /tasks/feed page
    And I should see "cat fake_file.txt"
