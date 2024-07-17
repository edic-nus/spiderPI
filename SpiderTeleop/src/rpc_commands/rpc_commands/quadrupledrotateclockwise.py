#run quadrupledstand before this

import requests
import json

def send_rpc_request(method, params, rpc_id=17):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"Move",
    "params":[4, 0, 20, 200, 0],
    #<mode>, <movement_direction>, <rotation>, <speed>, <times> 
    "jsonrpc" : "2.0", 
    "id": 17
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("Move", [4, 0, 20, 200, 0], rpc_id=17)
print(response)