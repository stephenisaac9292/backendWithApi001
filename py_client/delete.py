import requests
product_id = input("Enter the product id you want to delete : \n")
try:
    product_id=int(product_id)
except:
    print (f'product id {product_id} is not valid; please enter a valid product id')

if product_id:
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    get_response = requests.delete(endpoint) 
    print(get_response.status_code == 204)



