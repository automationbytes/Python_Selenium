Feature: Simple program to Search Something on Google

  @sanity
  Scenario Outline: : Google Search

    Given the user launches "google" url
    When the user is on google homepage
    Then the user searches "<search>" in searchbox
    And the user clicks enter

    Examples:
    |search|
    |google|
    |selenium|
    |python  |

  @regression
  Scenario: Python Search

    Given the user launches "bing" url
    #When the user is on google homepage
    Then the user searches "Python" in searchbox
    And the user clicks enter