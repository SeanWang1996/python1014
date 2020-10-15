import requests
import random

# 改成你自己的
base_url ='https://ucom20201015.firebaseio.com/%s.json'

url4 = base_url % 'buying_list'
stores = ['7-11', 'fami', 'OK', "Hi-life"]

for _ in range(10):
    record = {'store': random.choice(stores), 'quantity': random.randint(10, 20)}
    result = requests.post(url4, json=record)
    print(result.status_code, result.json())

