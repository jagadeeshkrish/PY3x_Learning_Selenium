from selenium import webdriver
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



@pytest.mark.Positive
@allure.title("VWO Invalid Login Page -test_Mini_project_2")
@allure.description("Verify the Invalid Email, Password. Error message came")
def test_Mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"
    #id -> name-> classname -> link/partial -> tagname -> css selector -> xpath.
    #-Find the Email,Password and enter the invalid details
    #< input
    #type = "email"
    #class ="text-input W(100%)"
    #name="username"
    #id="login-username"
    #data-qa="hocewoqisi"
    #>
    email_webelement = driver.find_element(By.ID,"login-username")
    email_webelement.send_keys("admin@admin.com")
    time.sleep(100)

    #driver.quit()
