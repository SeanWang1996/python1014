# import time
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# URL1 = "https://www.uuu.com.tw"
# browser = Chrome()
# browser.get(URL1)
# element = browser.find_element_by_class_name("BTN-Alert-Close")
# element.click()
# element = browser.find_element_by_class_name("fas.fa-search")
# element.click()
# time.sleep(5)
# element = browser.find_element_by_class_name("SearchTextBOX")
# element.clear()
# element.send_keys("android")
# element.send_keys(Keys.RETURN)
# time.sleep(100)
# browser.close()
# import time
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
# URL1 = "https://www.uuu.com.tw"
# browser = Chrome()
# browser.get(URL1)
# element = browser.find_element_by_class_name("BTN-Alert-Close")
# element.click()
# element = browser.find_element_by_class_name("fas.fa-search")
# element.click()
# time.sleep(2)
# element = browser.find_element_by_class_name("SearchTextBOX")
# element.clear()
# element.send_keys("python")
# element.send_keys(Keys.RETURN)
# time.sleep(2)
# courses = browser.find_elements_by_tag_name("h3")
# for course in courses:
#     print(course.text)
# browser.close()

# import time
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
#
# URL1 = "https://www.momoshop.com.tw/main/Main.jsp"
# browser = Chrome()
# browser.get(URL1)
# time.sleep(2)
# element = browser.find_element_by_id("keyword")
# element.clear()
# element.send_keys("洗潔精")
# element.send_keys(Keys.RETURN)
# time.sleep(5)
# area = browser.find_element_by_class_name("listArea")
# print(type(area))
# products = area.find_elements_by_class_name("goodsUrl")
# print(f"total {len(products)} products")
# for p in products:
#     print(p.get_property("href"))
#     productName = p.find_element_by_class_name("prdName")
#     print(productName.text)
# browser.close()
# import time
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.keys import Keys
#
# URL1 = "https://shopping.pchome.com.tw/"
# browser = Chrome()
# browser.get(URL1)
# time.sleep(10)
# element = browser.find_element_by_id("keyword")
# element.clear()
# element.send_keys("洗潔精")
# element.send_keys(Keys.RETURN)
# time.sleep(20)
# browser.close()
# import time
#
# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# URL1 = "https://shopping.pchome.com.tw/"
# browser = Chrome()
# browser.get(URL1)
# time.sleep(30)
# browser.refresh()
# time.sleep(2)
# element = browser.find_element_by_id("keyword")
# element.clear()
# element.send_keys("洗潔精")
# element.send_keys(Keys.RETURN)
# element = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.ID, "ItemContainer"))
# )
# print(type(element))
# items = element.find_elements_by_class_name("col3f")
# for item in items:
#     nick = item.find_element_by_class_name("nick")
#     print(nick.text)
# browser.close()
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# URL1 = "https://shopping.pchome.com.tw/"
# browser = Chrome()
# browser.get(URL1)
# time.sleep(2)
# # browser.refresh()
# # time.sleep(2)
# while True:
#     try:
#         element = browser.find_element_by_id("keyword")
#     except:
#         browser.refresh()
#         time.sleep(2)
#     else:
#         break
#
# element = browser.find_element_by_id("keyword")
# element.clear()
# element.send_keys("洗潔精")
# element.send_keys(Keys.RETURN)
# element = WebDriverWait(browser, 10).until(
#     EC.presence_of_element_located((By.ID, "ItemContainer"))
# )
# print(type(element))
# items = element.find_elements_by_class_name("col3f")
# for item in items:
#     nick = item.find_element_by_class_name("nick")
#     print(nick.text)
# browser.close()



# s1 = set() #兩者印出的東西不太一樣，但型別都是set，可以注意一下
# print(s1)
# s2 = {} #兩者印出的東西不太一樣，但型別都是set，可以注意一下
# print(s2)
# s3 = set(range(5))
# print(s3)
# s4 = {1, 1, 2, 1} #可以注意當印出的時候只剩下不重複的元素，也就是只剩1,2而已
# print(s4)
# s5 = set("aquickbrownfox")
# print(s5)
# class Course:
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
#
#
# c1 = Course("POOP", 35)
# c2 = Course("POOP", 35)
# c3 = c1
# c4 = Course("BDPY", 35)
# print(c1 is c2, c1 is c3, c1 is c4)
# print(c1 == c2, c1 == c3, c1 == c4)
# s1 = {c1}
# print(f"[1]s1={s1}")
# s1.add(c3)
# print(f"[2]s1={s1}")
# s1.add(c2)
# print(f"[3]s1={s1}")
# class Course:
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
#
#     # add __str__ and __repr__
#     def __str__(self):
#         return f"course name={self.name}, duration={self.duration}"
#
#     def __repr__(self):
#         return str(self)
#
#     def __eq__(self, other):
#         return self.name == other.name and self.duration == other.duration
#
#
# c1 = Course("POOP", 35)
# c2 = Course("POOP", 35)
# c3 = c1
# c4 = Course("BDPY", 35)
# print(c1 is c2, c1 is c3, c1 is c4)
# print(c1 == c2, c1 == c3, c1 == c4)
# s1 = {c1}
# print(f"[1]s1={s1}")
# s1.add(c3)
# print(f"[2]s1={s1}")
# s1.add(c2)
# print(f"[3]s1={s1}")
class Course:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    # add __str__ and __repr__
    def __str__(self):
        return f"course name={self.name}, duration={self.duration}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and self.duration == other.duration

    def __hash__(self):
        return hash((self.name, self.duration))


c1 = Course("POOP", 35)
c2 = Course("POOP", 35)
c3 = c1
c4 = Course("BDPY", 35)
print(hash(c1))
print(hash(c2))
print(hash(c3))
print(hash(c4))
print(c1 is c2, c1 is c3, c1 is c4)
print(c1 == c2, c1 == c3, c1 == c4)
s1 = {c1}
print(f"[1]s1={s1}")
s1.add(c3)
print(f"[2]s1={s1}")
s1.add(c2)
print(f"[3]s1={s1}")
s1.add(c4)
print(f"[4]s1={s1}")
