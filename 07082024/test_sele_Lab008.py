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
    # < input
    # type = "email"
    # class ="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >
    email_web_element = driver.find_element(By.NAME, "username")
    email_web_element.send_keys("admin@admin.com")
    time.sleep(10 )
    # <input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe">

    Password_web_element = driver.find_element(By.CSS_SELECTOR,"[data-qa='hocewoqisi']")
    Password_web_element.send_keys("admin@123")
    time.sleep(5 )
    #<button type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">
	#<span class="icon loader hidden" data-qa="zuyezasugu"></span>
	#<span data-qa="ezazsuguuy">Sign in</span>
	#</button>
    submit_web_element=driver.find_element(By.ID,"js-login-btn")
    submit_web_element.click()
    time.sleep(5)
    error_message_web_element=driver.find_element(By.ID,"js-notification-box-msg")
    assert error_message_web_element.text=="Your email, password, IP address or location did not match"
    time.sleep(5)
    driver.quit()