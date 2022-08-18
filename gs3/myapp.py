import requests
import json

URL = "http://127.0.0.1:8000/stdget/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(URL,data=json_data)
    data = r.json()
    print(data)


# get_data(2)

def post_data():
    data ={
        'name':'ravi',
        'roll':104,
        'city': 'Chennai'
    }

    json_data = json.dumps(data)
    r = requests.post(URL,data=json_data)
    data = r.json()
    print(data)

# post_data()



def update_data():
    data ={
        'id':4,
        'name':'Gaurav',
        'city': 'Panjab'
    }

    json_data = json.dumps(data)
    r = requests.put(URL,data=json_data)
    data = r.json()
    print(data)

# update_data()



def delete_data(id = None):
    data ={'id': id}

    json_data = json.dumps(data)
    r = requests.delete(URL,data=json_data)
    data = r.json()
    print(data)

delete_data(2)