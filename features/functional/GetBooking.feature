Feature: Get Booking Validations

  Background: Auth token is generated
    Given Auth token is generated successfully

  Scenario Outline: Verify get booking api when valid details are sent in request
    Given <booking_id> is provided
    When get booking api is executed
    Then verify <firstname>
    And verify status code as 201

    Examples:
    |booking_id | firstname   |
    | 1         | Manoj       |