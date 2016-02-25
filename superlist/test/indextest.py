
from selenium import webdriver

dr = webdriver.Chrome()

dr.get("http://127.0.0.1:8000")

assert 'Django' in dr.title

dr.quit()