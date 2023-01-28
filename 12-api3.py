import requests
import json
BASE_URL="http://host1.open.uom.lk:8080"

update={
    "brand":"Araliya",
}

response=requests.put(f"{BASE_URL}/api/products/",json=update)

print(response.json())