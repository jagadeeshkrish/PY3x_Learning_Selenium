from selenium import webdriver
import pytest
import allure
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



@pytest.mark.Positive
@allure.title("Verify that URL canges when we click on the make appointment Button")
@allure.description("Verify the URL changes")
def test_Mini_project_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    #-Find the element the anchor tag
    #we need to find unique attribute which can finr the web element
    #-Click on it
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    #Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    driver.quit()
