import requests

endpoint = "http://localhost:8000/api/products/update/2/"
data = {
    "title": "this is data after update",
    "price" : 1000.00,
}

get_response = requests.put(endpoint , json= data) # update = put  , create = post , delete = delete , get = get
print(get_response.json())