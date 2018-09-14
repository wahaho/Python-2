from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("selenium + python")
driver.find_element_by_id("su").click()




# from selenium import webdriver
#
# browser = webdriver.Firefox()
# browser.get("http://www.baidu.com")
# browser.find_element_by_id("kw").send_keys("Eric_guodongliang")
# browser.find_element_by_id("su").submit()


#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait