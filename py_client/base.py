import requests



# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


respone = requests.get(endpoint, json={"query":"hello world"}) # Application Programming Interface (API) simple one 

print (respone.json()) 



# what you send is similar to what you recieve 