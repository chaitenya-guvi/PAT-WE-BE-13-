import requests

url = "https://reqres.in/"
url2 = "https://reqres.in/api/users/2"

response = requests.get(url2)

print(response.status_code)
print(response.text)