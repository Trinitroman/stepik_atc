from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome() 
    browser.get(link)
    
    ft = browser.find_element(By.ID, "num1").text
    sd = browser.find_element(By.ID, "num2").text
    res = str(int(ft)+int(sd))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(res)
   
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