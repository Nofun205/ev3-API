import requests

class ClienteAPI:
    base_url = "https://jsonplaceholder.typicode.com"

    @staticmethod
    def get(endpoint):
        return requests.get(f"{ClienteAPI.base_url}/{endpoint}")

    @staticmethod
    def post(endpoint, data):
        return requests.post(f"{ClienteAPI.base_url}/{endpoint}", json=data)
    
    