from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_open_vwologin():
    driver = webdriver.Chrome()
    #driver = webdriver.remote("ipaddress")
    driver.get("https://app.vwo.com")
    print(driver.page_source)
    driver.refresh()
    driver.back()
    driver.forward()
    #driver.close()
    # will only close the current tab,
    # session id!=Null,
    # it will not close the other tabs
    time.sleep(10)
    driver.quit()
    # will closes all the tabs,
    # session id ==Null,
