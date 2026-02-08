Feature: SauceDemo Login

  Scenario: Valid Login
    Given user opens SauceDemo login page
    When user enters valid username and password
    Then user should land on inventory page
