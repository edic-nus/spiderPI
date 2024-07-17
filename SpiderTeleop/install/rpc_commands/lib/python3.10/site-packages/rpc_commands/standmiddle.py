import requests
import json

def send_rpc_request(method, params, rpc_id=13):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"Stand",
    "params":[100,2,1],
    # <Height>, <mode>, <time>
    "jsonrpc" : "2.0", 
    "id": 13
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("Stand", [100,2,1], rpc_id=13)
print(response)
