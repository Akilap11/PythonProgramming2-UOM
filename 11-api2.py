import requests

BASE_URL= "http://host1.open.uom.lk:8080"

response=requests.get(f"{BASE_URL}/api/products/")
data=response.json()['data']

Jres=response.json()
print(len(response.json()["data"]))
