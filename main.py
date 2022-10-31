import json
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://food.grab.com/sg/en/restaurants")

driver.maximize_window()