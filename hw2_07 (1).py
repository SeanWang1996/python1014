##
# 姓名:王昱翔
# 座位號碼:07
# 修改檔名到你的座位號碼
##

import time

# search pytorch



from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

URL = "https://www.python.org"
STRING = "pytorch"
browser = Chrome()
browser.get(URL)
time.sleep(1)
# continue to finish
# remember to search pytorch
element = browser.find_element_by_name('q')
element.clear()
element.send_keys(STRING)
element.send_keys(Keys.RETURN)
time.sleep(1)
element = browser.find_elements_by_css_selector(".list-recent-events.menu")
allItems = element[0].find_elements_by_tag_name("li")
for item in allItems:
    content = item.find_element_by_tag_name('a')
    print(content.text)
element = browser.find_elements_by_css_selector(".list-recent-events.menu")
allItems1 = element[0].find_elements_by_tag_name("li")
for item in allItems1:
    content1 = item.find_element_by_tag_name('p')
    content2 = item.find_element_by_tag_name('#text')
    print(content1.text)
    print(content2.text)
browser.close()
