import requests
from getpass import getpass

auth_endpoint  = "http://localhost:8000/api/auth/"
username = input("Username: ")
password = getpass()
data = {"username" :username , "password":password}
auth_respone = requests.post(auth_endpoint , json= data)
print (auth_respone.json())
if auth_respone.status_code == 200:
    token = auth_respone.json()['token']
    headers = {"Authorization": f"Bearer {token}"}
    endpoint  = "http://localhost:8000/api/products/"
    get_response = requests.get(endpoint , headers=headers)
    print (get_response.json())

