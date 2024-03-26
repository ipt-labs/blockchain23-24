import argparse
import requests
import json

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--method")
ap.add_argument("-p", "--params")
args = vars(ap.parse_args())

# print(args['params'])

session = requests.Session()
method = args['method']
params = args['params']
if params != None: 
    params = params.split(' ')

print(params)

payload= {"jsonrpc":"2.0",
           "method":method,
           "params":params,
           "id":1}

headers = {'Content-type': 'application/json'}
response = session.post('http://localhost:8545', json=payload, headers=headers)
try:
    print(json.dumps(response.json()['result'], indent=1))
except Exception as err:
    print('some problem ocured:', err)
    print(json.dumps(response.json(), indent=1))

#print('network id: ', response.json()['result'])

# '''
# curl --location --request POST 'localhost:8545' \
# --header 'Content-Type: application/json' \
# --data-raw '{
#     "jsonrpc": "2.0",
#     "id": 1,
#     "method": "admin_peers",
#     "params": []
# }'
# '''