Feature: Create Booking Validations

  Background: Auth token is generated
    Given Auth token is generated successfully

  Scenario Outline: Verify create booking api when valid details are sent in request
    Given <firstname> <lastname> <totalprice> <depositpaid> <checkin> <checkout> <additionalneeds> are provided
    When create booking api is executed
    Then verify <firstname>
    And verify status code as 201

    Examples:
    |firstname | lastname   | totalprice | depositpaid | checkin    | checkout   | additionalneeds |
    |Manoj     | Kumar      | 123        | True        | 2023-12-10 | 2023-12-13 | Breakfast       |
    |Rohit     | Kumar      | 457        | True        | 2023-12-11 | 2023-12-15 | Lunch           |
    |Seema     | Ahlawat    | 987        | True        | 2023-12-13 | 2023-12-18 | Dinner          |
    |Sachin    | Kumar      | 222        | True        | 2023-12-15 | 2023-12-16 | Breakfast       |