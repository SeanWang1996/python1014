import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
URL1 = "https://www.uuu.com.tw"
browser = Chrome()
browser.get(URL1)
element = browser.find_element_by_class_name("BTN-Alert-Close")
element.click()
element = browser.find_element_by_class_name("fas.fa-search")
element.click()
# element = browser.find_element_by_id("keyword")
# element.clear()
# element.send_keys("洗潔精")
# element.send_keys(Keys.RETURN)
time.sleep(10)
browser.close()