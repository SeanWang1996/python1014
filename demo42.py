# import requests, bs4
#
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
#     print(url1+link.get('href'))
from urllib.request import urlopen

from PIL import Image

url1 = "https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-2020-10-15-11-20.jpg"
# 手動建立images
endpoing1 = urlopen(url1)
image = Image.open(endpoing1)
image.save('images/demo44.jpg')
halfSize = (image.size[0] // 2, image.size[1] // 2)
halfImage = image.resize(halfSize, Image.ANTIALIAS)
halfImage.save('images/demo44_half.jpg')
rot90 = image.transpose(Image.ROTATE_90)
rot90.save('images/demo44_90.jpg')
rot45 = image.rotate(45)
rot45.save('images/demo44_45.jpg')