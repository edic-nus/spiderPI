import requests
import json

def send_rpc_request(method, params, rpc_id=10):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"Stand",
    "params":[50,2,5],
    # <Height>, <mode>, <time>
    "jsonrpc" : "2.0", 
    "id": 10
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("Stand", [50,2,5], rpc_id=10)
print(response)