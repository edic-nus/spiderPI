import requests
import json

def send_rpc_request(method, params, rpc_id=3):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"StopActionGroup",
    "params":[],
    "jsonrpc" : "2.0", 
    "id": 3
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("StopActionGroup", [], rpc_id=3)
print(response)
