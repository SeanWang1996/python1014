# import shutil
# import json
#
# # shutil.copytree('graph','graph3')
# # shutil.rmtree('graph3')
#
#
# a1 = [500, 'Hi', '中文輸入', None, [3, 4, 5]]
# b1 = {"Name": '''Mark''', "Location": '台北', "Role": "Instructor"}
# print(type(a1), type(b1))
# a2 = json.dumps(a1)
# b2 = json.dumps(b1)
# print(type(a2), type(b2))
# print(a1)
# print(a2)
# print(b1)
# print(b2)
# print(a2[:10])
# a3 = json.loads(a2)
# b3 = json.loads(b2)
# print(type(a3), type(b3))
#
# print(a3)
# print(b3)

import requests

url1 = "https://bugzilla.mozilla.org/rest/bug/35"
response = requests.get(url1)
print(type(response))
print(response.status_code)
print(response.headers['content-type'])
print(type(response.content))
print(type(response.json()))

for k, v in response.json().items():
    print(k, v)

bugs = response.json()['bugs']
firstBug = bugs[0]
print(firstBug['summary'])
print(firstBug['assigned_to_detail']['id'])
print(firstBug['cc_detail'][0], firstBug['cc_detail'][4])