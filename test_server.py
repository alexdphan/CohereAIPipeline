import requests

response = requests.get("http://localhost:8000/preprocess", params={"text": "This is a test sentence."})
print(response.json())