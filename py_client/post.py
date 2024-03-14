import requests

endpoint  = "http://localhost:8000/api/products/"
data = {"title" : "lets see what is happen now"}
get_response = requests.post(endpoint , json = data)
print (get_response.json())