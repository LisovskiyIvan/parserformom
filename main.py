import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import pandas as pd
from data import inns
import os

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome(options=options)
path = r"C:\Users\johnyjabrony\Downloads"

try:
    # book = pd.read_excel("parserformom/test3.xlsx", usecols="b")
    # data = book.values.tolist()
    # for z in data:
    #     for i in z:
    for i in inns:
            print(i)
            driver.get("https://egrul.nalog.ru/index.html")
            
            input_id = driver.find_element(By.ID, "query")
            input_id.send_keys(i)
            search_btn = driver.find_element(By.ID, "btnSearch").click()
            time.sleep(2)
            get_btn = driver.find_element(By.CLASS_NAME, "btn-excerpt").click()
            time.sleep(1)
            new_name = driver.find_element(By.CLASS_NAME, "op-excerpt").text
            time.sleep(1)
            

             # Путь к вашей папке
            name_str = rf'C:\Users\johnyjabrony\Downloads\{new_name}.pdf'
            # Получим список имен всего содержимого папки
            # и превратим их в абсолютные пути
            dir_list = [os.path.join(path, x) for x in os.listdir(path)]

            if dir_list:
                # Создадим список из путей к файлам и дат их создания.
                date_list = [[x, os.path.getctime(x)] for x in dir_list]

                # Отсортируем список по дате создания в обратном порядке
                sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)

                # Выведем первый элемент списка. Он и будет самым последним по дате .strip(r"C:\Users\johnyjabrony\Downloads")
                old_name = sort_date_list[0][0]
                name_str = name_str.replace('"', '').replace('ПУБЛИЧНОЕ', 'П').replace('АКЦИОНЕРНОЕ', 'А').replace('ОБЩЕСТВО', 'О')
            os.rename(old_name, name_str.replace('"', ''))

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
