import requests

URL = "http://127.0.0.1:8000/stdall/"   # url to send our request 

receive = requests.get(url = URL)    # get request to url  

data = receive.json()    # Extract data 

print(data)




# this is python application which will communicate with api 