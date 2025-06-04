import requests

endpoint = "http://127.0.0.1:8000/api/products/11/update/"
data = {
    'title': 'Forza',
    'content': 'Elemento de prueba',
    'price': 45,
}
get_response = requests.put(endpoint, json = data) 
print(get_response.json())



