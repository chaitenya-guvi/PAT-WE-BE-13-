import requests

url = "https://icanhazdadjoke.com/"
# url2 = "https://www.google.com/search?q=guvi"

response = requests.get(url, headers={"Accept": "application/json"})

# print(response.text)
# print(type(response.text))
data = response.json()
print(data)
print(type(data))
print(data["joke"])
print(f"status: {data['status']}")
