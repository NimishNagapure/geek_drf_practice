import requests
import json

URL = "http://127.0.0.1:8000/stdapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.get(URL,headers=headers, data=json_data)
    data = r.json()
    print(data)


# get_data()


def post_data():
    data ={
        'name':'Nhali',
        'roll':112,
        'city': 'Pune'
    }

    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.post(URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# post_data()



def update_data():
    data ={
        'id':5,
        'name':'Chiku',
        'city': 'Pune'
    }

    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.put(URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# update_data()



def delete_data(id = None):
    data ={'id': id}

    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    r = requests.delete(URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

delete_data(5)