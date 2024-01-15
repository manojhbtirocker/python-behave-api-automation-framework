from behave import *


@given('{username} and {password}')
def step_impl(context, username, password):
    print('username' + username)
    print('password' + password)


@when('auth api is executed')
def step_impl(context):
    print('inside auth api is executed')


@then('verify token details')
def step_impl(context):
    print('Inside verify token details')


@then('verify status code as {statusCode:d}')
def step_impl(context, statusCode):
    print(statusCode)


@then('verify error message')
def step_impl(context):
    print('inside verify error message')


@given('Auth token is generated successfully')
def step_impl(context):
    print('Inside Auth token is generated successfully')


@given('{firstname} {lastname} {totalprice:d} {depositpaid} {checkin} {checkout} {additionalneeds} are provided')
def step_impl(context, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    print('Inside user details are provided')


@when('create booking api is executed')
def step_impl(context):
    print('Inside create booking api is executed')


@then('verify {firstname}')
def step_impl(context, firstname):
    print('Inside verify firstname')


@given('{booking_id:d} is provided')
def step_impl(context, booking_id):
    print('inside booking id step')


@when('get booking api is executed')
def step_impl(context):
    print('Inside get booking id')


@given('{booking_id} {firstname} {lastname} {totalprice:d} {depositpaid} {checkin} {checkout} {additionalneeds} are '
       'present')
def step_impl(context, booking_id, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    print('Inside update api')


@when('update booking api is executed')
def step_impl(context):
    print('Inside update api call')
