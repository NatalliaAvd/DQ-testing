import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера.
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://projectby.trainings.dlabanalytics.com/nkavalen93/")
time.sleep(5)

# Найдем кнопку
button = driver.find_element(By.ID, "kc-social-providers")

# нажать на кнопку
button.click()
time.sleep(5)

driver.get("https://projectby.trainings.dlabanalytics.com/nkavalen93/notebooks/Testing.ipynb")
time.sleep(5)

run_button = driver.find_element_by_css_selector("#run_int > button:nth-child(1)")
run_button.click()
time.sleep(5)


# закрыть окно браузера
driver.quit()






