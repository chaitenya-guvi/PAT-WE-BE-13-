Feature: SauceDemo Login

  Background:
    Given user opens SauceDemo login page

  Scenario: Valid Login
    When user enters valid username and password
    Then user should land on inventory page

  Scenario: Invalid Login
    When user enters invalid username and password
    Then user should see error message
