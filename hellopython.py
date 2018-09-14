# coding:utf-8
from selenium import webdriver

driver = webdriver.Safari()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium + python")
driver.find_element_by_id("su").click()

#
# class ABC:
#     def __init__(self):
#         print ("ds")
#     def ok(self):
#         print ("hello")
#
# if True:
#     print ("True")
# else:
#     print ("False")
# # driver.quit()
# # driver.close()

