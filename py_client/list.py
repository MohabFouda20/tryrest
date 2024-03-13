import requests

endpoint  = "http://localhost:8000/api/products/"
# data = {"title" : "i will done here soon"}
get_response = requests.get(endpoint)
print (get_response.json())