import requests


class ApiCalls:

    def createAuthToken(self):
        self.url = 'https://restful-booker.herokuapp.com/auth'
        self.data = {"username": "admin", "password": "password123"}
        self.headers = {"Content-Type": "application/json"}
        auth_response = requests.post(url=self.url, json=self.data, headers=self.headers)
        print(auth_response.json())
        return auth_response.json()['token']

    def createBooking(self):
        self.url = 'https://restful-booker.herokuapp.com/booking'
        self.data = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True,"bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}
        self.headers = {"Content-Type": "application/json"}
        create_response = requests.post(url=self.url, json=self.data, headers=self.headers)
        print(create_response.json())
        return create_response.json()['bookingid']

    def updateBooking(self, booking_id):
        self.url = 'https://restful-booker.herokuapp.com/booking/{}'.format(booking_id)
        self.data = {"firstname": "manoj", "lastname": "Brown", "totalprice": 111, "depositpaid": True,"bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}
        self.headers = {"Content-Type": "application/json", "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="}
        update_response = requests.put(url=self.url, json=self.data, headers=self.headers)
        print(update_response.json())
        return update_response.json()['firstname']

    def getBooking(self, booking_id):
        self.url = 'https://restful-booker.herokuapp.com/booking/{}'.format(booking_id)
        get_response = requests.get(url=self.url)
        print(get_response.json())

    def deleteBooking(self, booking_id):
        self.url = 'https://restful-booker.herokuapp.com/booking/{}'.format(booking_id)
        self.headers = {"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="}
        delete_response = requests.delete(url=self.url, headers=self.headers)
        print(delete_response.status_code)


api_calls = ApiCalls()

auth_token = api_calls.createAuthToken()
booking_id = api_calls.createBooking()
print(booking_id)
first_name = api_calls.updateBooking(booking_id)
print(first_name)
api_calls.getBooking(booking_id)
api_calls.deleteBooking(booking_id)
