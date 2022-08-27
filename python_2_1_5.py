from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome() 
browser.get(link)

try:
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()
    
    radiobox1 = browser.find_element(By.ID, "robotsRule")
    radiobox1.click()
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