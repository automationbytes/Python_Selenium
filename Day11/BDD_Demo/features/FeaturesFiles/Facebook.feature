Feature: Facebook Login

  @regression
  Scenario Outline: To login into facebook

  Given the user launches "facebook" url
  Then user enter Username as "<username>" and Password as "<password>"
  Then user clicks on submit

    Examples:
     |username|password|
     |user1|Pwd1|
     |user2|pwd2|

  @sanity
  Scenario Outline: To login google

    Given the user launches "<url>" url
    Examples:
    |url|
    |google|
    |bing  |
    |amazon|