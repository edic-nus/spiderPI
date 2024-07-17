import requests
import json

def send_rpc_request(method, params, rpc_id=4):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"Transport",
    "params":[2],
    "jsonrpc" : "2.0", 
    "id": 4 
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("Transport", [2], rpc_id=4)
print(response)