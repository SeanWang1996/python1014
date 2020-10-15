import requests

base_url = 'https://ucom20201015.firebaseio.com/%s.json'
url1 = base_url % 'demo1'
url2 = base_url % 'demo2_list'
url3 = base_url % 'demo3_dict'
url4 = base_url % 'buying_list'
r1 = requests.get(url1)
print(r1.status_code, type(r1.json()), r1.json())
r2 = requests.get(url2)
print(r2.status_code, type(r2.json()), r2.json())
r3 = requests.get(url3)
print(r3.status_code, type(r3.json()), r3.json())
r4 = requests.get(url4)
#print(r4.json())
for v in r4.json().values():
    print(v['quantity'])
requests.delete(url1)
requests.delete(url2)
requests.delete(url3)
requests.delete(url4)
