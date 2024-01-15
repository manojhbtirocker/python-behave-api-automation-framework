Feature: Auth Token Validations

  Scenario Outline: Verify Auth Token api when valid username and password are sent in request
    Given <username> and <password>
    When auth api is executed
    Then verify token details
    And verify status code as 201

    Examples:
    |username | password   |
    |admin    | password123|
    |aaa      | qqq        |

  Scenario Outline: Verify Auth Token api when invalid username and password are sent in request
    Given <username> and <password>
    When auth api is executed
    Then verify error message
    And verify status code as 400

    Examples:
    |username | password |
    |admin    | pass123  |