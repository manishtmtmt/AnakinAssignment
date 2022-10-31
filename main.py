import json
from selenium import webdriver
from time import sleep

# Opening the website on Chrome
driver = webdriver.Chrome()
driver.get("https://food.grab.com/sg/en/restaurants")

driver.maximize_window()

# Function for append data to json file
def write_json(new_data, filename='restaurants.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data['restaurants'].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)

