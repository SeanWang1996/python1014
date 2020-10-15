import requests, bs4

# url1 = "https://www.uuu.com.tw/"
#
# r1 = requests.get(url1)
# soup1 = bs4.BeautifulSoup(r1.content, "html.parser")
# print(type(soup1), soup1.title.name, soup1.title.string)
#
# courseLists = soup1.find('div', {'id': 'course_list'})
# for course in courseLists:
#     print(type(course), course)
# print("--------------")
# courseLinks = courseLists.find_all('a')
# for link in courseLinks:
#     print(link.p)
#     print(link.p.text)
#     print(url1+link.get('href'))

# 改成你自己的

import time

import requests

# 改成你自己的
base_url ='https://ucom20201015.firebaseio.com/%s.json'

url1 = base_url % 'demo1'


r1 = requests.put(url1, json='hello python to firebase')
print(r1.status_code, r1.json())
url2 = base_url % 'demo2_list'
r2 = requests.put(url2, json=['Jan', 'Feb', None, None, 'May'])
print(r2.status_code, r2.json())
url3 = base_url % 'demo3_dict'
r3 = requests.put(url3, json={'name': 'bdpy', 'duration': 500})
print(r3.status_code, r3.json())