import requests
url = input("Enter the API URL: ")
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Failed to retrieve data")