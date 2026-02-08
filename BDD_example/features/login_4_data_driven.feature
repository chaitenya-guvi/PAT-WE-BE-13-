Feature: SauceDemo Login

  Background:
    Given user opens SauceDemo login page

  Scenario Outline: Login with multiple users
    When user enters username "<username>" and password "<password>"
    Then login result should be "<result>"

  Examples:
    | username          | password       | result        |
    | standard_user     | secret_sauce   | success       |
    | locked_out_user   | secret_sauce   | locked_error  |
