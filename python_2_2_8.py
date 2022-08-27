from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
  
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome() 
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("1")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("2")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("3")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name="file.txt"   
    file_path = os.path.join(current_dir, file_name)      
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()
   

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    browser.close()
    # закрываем браузер после всех манипуляций
    browser.quit()