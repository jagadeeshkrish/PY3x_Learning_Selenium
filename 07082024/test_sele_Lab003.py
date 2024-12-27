from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_open_vwologin():
    chrome_options = Options()
    chrome_options.add_extension("C:/Users/jagad/Downloads/adblock.crx")
    #chrome_options.add_argument("--page-load-strategy=eager")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.youtube.com")
    driver.maximize_window()
    #driver.get("https://app.vwo.com")
    #driver = webdriver.Edge()
    time.sleep(10)
