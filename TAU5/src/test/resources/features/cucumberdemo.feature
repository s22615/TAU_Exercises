Feature: Test log in to Reddit page
  Scenario: User gives wrong data to log in.
    Given Login page
    When User tries to enter his login data
    Then He should received that data is wrong