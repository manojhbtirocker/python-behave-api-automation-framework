Feature: Update Booking Validations

  Background: Auth token is generated
    Given Auth token is generated successfully

  Scenario Outline: Verify update booking api when valid details are sent in request
    Given <booking_id> <firstname> <lastname> <totalprice> <depositpaid> <checkin> <checkout> <additionalneeds> are present
    When update booking api is executed
    Then verify <firstname>
    And verify status code as 201

    Examples:
    |booking_id |firstname | lastname   | totalprice | depositpaid | checkin    | checkout   | additionalneeds |
    |  1        |Manoj     | Kumar      | 123        | True        | 2023-12-10 | 2023-12-13 | Breakfast       |
    |  2        |Rohit     | Kumar      | 457        | True        | 2023-12-11 | 2023-12-15 | Lunch           |
    |  3        |Seema     | Ahlawat    | 987        | True        | 2023-12-13 | 2023-12-18 | Dinner          |
    |  4        |Sachin    | Kumar      | 222        | True        | 2023-12-15 | 2023-12-16 | Breakfast       |