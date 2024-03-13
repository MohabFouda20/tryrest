import requests
id = input("Enter the id of the product you want to delete: ")
try :
    product_id = int(id)
except:
    product_id = None
    print (f"Invalid id {id} please enter a number")
if product_id is not None:
    endpoint = f"http://localhost:8000/api/products/delete/{product_id}/"


    get_response = requests.delete(endpoint)
    status_code = get_response.status_code()
    print(status_code)
    if status_code == 204:
        print("done")
    else:
        print("not found")
