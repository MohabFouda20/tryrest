import requests

# Set the endpoint URL
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# Make a POST request to the endpoint with JSON data
response = requests.post(endpoint, json={"title": "hey" , "content": "hello" , "price": 123.45}) # This is a POST request and change by changig the method


if response.status_code == 200:
    print("Request was successful:")
    print(response.json())  # Print the JSON response
else:
    print("Request failed with status code:", response.status_code)
