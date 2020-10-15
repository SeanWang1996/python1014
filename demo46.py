import requests

# 改成你自己的
base_url ='https://ucom20201015.firebaseio.com/%s.json'

url1 = base_url % 'demo1'


url2 = base_url % 'demo2_list'
requests.patch(url2, json={"2":"Mar","3":"Apr","4":"五月"})
url3 = base_url % 'demo3_dict'
requests.patch(url3,json={'duration':35,"instructor":"Mark Ho"})
