import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
URL1 = "https://www.momoshop.com.tw/main/Main.jsp"
browser = Chrome()
browser.get(URL1)
element = browser.find_element_by_id("keyword")
element.clear()
element.send_keys("洗潔精")
element.send_keys(Keys.RETURN)
time.sleep(10)
browser.close()