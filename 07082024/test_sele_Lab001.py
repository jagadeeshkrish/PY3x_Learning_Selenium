from selenium import webdriver
import time

def test_sample():
    driver = webdriver.Edge()
    #driver.get("https://google.com")
    #assert driver.current_url == "https://www.google.com/"
    print(driver.session_id ) #unique scession ID of 16 digits is created
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    time.sleep(10)