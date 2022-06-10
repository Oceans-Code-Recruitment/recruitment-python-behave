@ui
Feature: UI Example

  Scenario: Verify that the user is able to log in
    Given the user logs in with
      | email                       | password   |
      | jose.ig.cabrera.b@gmail.com | Testing123 |
    When the user clicks on Profile menu
    Then verifies that the Profile User Name is "Jose Cabrer"
