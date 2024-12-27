from selenium import webdriver
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



@pytest.mark.Positive
@allure.title("Open the signup URL of VWO.com -test_Mini_project_3")
@allure.description("Verify that clicking on the signup button url changes")
def test_Mini_project_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"
    #< a
    #href = "https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class ="text-link"
    # data-qa="bericafeqo" >
    # Start a free trial
    # < / a >
    #partial Linktest means contains
    #LINK_TEXT= exact match

    #anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free")
    anchor_tag_element.click()
    assert  driver.current_url =="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5 )
    driver.quit()