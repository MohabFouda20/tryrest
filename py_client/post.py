import requests
headers = {"Authorization" :'Bearer 30a76b272575d032b3b89090dc706452a6965fab'}
endpoint  = "http://localhost:8000/api/products/"
data = {"title" : "el gay halawa"}
get_response = requests.post(endpoint , json = data , headers=headers)
print (get_response.json())