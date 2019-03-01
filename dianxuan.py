
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://dun.163.com/trial/icon-click")
img = driver.find_element_by_xpath('//img[@class="yidun_bg-img"]')
pass