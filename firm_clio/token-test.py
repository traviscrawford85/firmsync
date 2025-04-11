import requests

access_token = "16474-KLxWcKbiIXYwbtb0iAn0FwN6xwIcIi8FSd"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json"
}

response = requests.get("https://app.clio.com/api/v4/contacts?limit=3", headers=headers)

if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
