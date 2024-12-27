from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_open_vwologin():
    # opiton class -
    # customize the behaviour of the browser during automated testing
    # Chrome -> headless or UI -> headless mode -no ui
    # disable gpe, add extension maximize,set window, 100 other options
    # before starting the browser
    #creaate an instance of Chromeoptions
    chrome_options = Options()
    #chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--headless")
    driver = (webdriver.Chrome(chrome_options))
    driver.maximize_window()
    driver.get("https://app.vwo.com")
    #driver = webdriver.Edge()
    time.sleep(10)
