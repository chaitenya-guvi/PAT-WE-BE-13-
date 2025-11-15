import requests
# url = "http://www.google.com"  #Uniform Resource Locator
#
# response = requests.get(url)
#
# print(f"your request to {url} came back w/ status code {response.status_code}")
# print(response.url)
# print(response.request)

# print(response.text)


url2 = "https://www.google.com/search?q=guvi"

response = requests.get(url2)
print(response.text)