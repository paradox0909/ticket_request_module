import requests


url = "https://google.com"

response = requests.get(url=url)
cookies = response.cookies

for cookie in cookies:
    print(f"{cookie.name}: {cookie.value}")
