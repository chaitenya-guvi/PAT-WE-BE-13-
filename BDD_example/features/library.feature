Feature: Verify book name added in Library.

  @positive @chaitenya
  Scenario: Verify Book name.
    Given Book details.
    Then Verify book name.

  @negative @chaitenya
  Scenario: Verify Author name.
    Given Author details.
    Then Verify author name.