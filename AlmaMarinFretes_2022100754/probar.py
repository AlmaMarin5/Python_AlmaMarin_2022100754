import requests

url = "http://localhost:5003/cliente"
data = {
    "ci": "5593006"
}

response = requests.post(url, json=data)
print(response.json())

