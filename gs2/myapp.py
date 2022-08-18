import requests
import json

url = 'http://127.0.0.1:8000/stdcr/'

data = {
 'name':'Nimish',
 'roll':101,
 'city':'Nagpur'
}

json_data =json.dumps(data)

r = requests.post(url, data=json_data)

data = r.json()

print(data)