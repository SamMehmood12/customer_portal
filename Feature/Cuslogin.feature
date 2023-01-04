@regression
Feature: As an end user i want to login to the cadency and view the dashboard page

  Background: : samra
    Given Launch the Browser
    When User is at login Page

   # @login @smoke
    Scenario: Successful login with valid scenarios
    Then User Enters abc123 and pJPAiUshc541
    Then User Clicks on Login Button
#
#    @login
#    Scenario Outline: Invalid Login Scenarios to Cadency loginPage
#      Then User Enters <Uname> and <Pword>
#      Then User Clicks on Login Button
#      Then Verify User Navigation to HomePage or Error.
#      Then Close the Browser
#
#      Examples:
#      | Uname | Pword |
#      | maxwell| Samra123@  |
#      | abc123 | pJPAiUshc541|
#
#    Scenario: Testing Logout
#      Then User Enters abc123 and pJPAiUshc541
#      Then User Clicks on Login Button
#      Then Click on Profile Thumbnail
#      Then Logout
#    Scenario: test

#sammffffffffffffffffff