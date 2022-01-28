import requests

url = 'https://reqres.in/api/users/2'

response = requests.get(url)

print(response.content)