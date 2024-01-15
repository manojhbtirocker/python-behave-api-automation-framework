import requests

response = requests.get(url='https://reqres.in/api/users?page=2')
print(response.json())

post_response = requests.post(url='https://reqres.in/api/users',
              data='{"name": "manoj","job": "leader"}')
print(post_response.json())

get_response = requests.get(url='https://reqres.in/api/users/7')
print(get_response.json())

put_response = requests.put(url='https://reqres.in/api/users/7', data='{"name": "manoj1","job": "abc"}')
print(put_response.json())

get_response = requests.get(url='https://reqres.in/api/users/7')
print(get_response.json())

delete_response = requests.delete(url='https://reqres.in/api/users/7')
print(delete_response.status_code)

get_response = requests.get(url='https://reqres.in/api/users/7')
print(get_response.json())



