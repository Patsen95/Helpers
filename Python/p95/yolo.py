import requests

url = "https://api.notion.com/v1/databases/Movies-dba2181f0917438093986b2a5e668259"

headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "authorization": "Patsen95"
}

response = requests.get(url, headers=headers)

print(response.text)
