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
path = os.path.expanduser('~/Downloads')
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
        
            name_str = rf'{path}\{new_name}.pdf'
            dir_list = [os.path.join(path, x) for x in os.listdir(path)]

            if dir_list:
                date_list = [[x, os.path.getctime(x)] for x in dir_list]
                sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
                old_name = sort_date_list[0][0]
                name_str = name_str.replace('"', '').replace('ПУБЛИЧНОЕ', 'П').replace('АКЦИОНЕРНОЕ', 'А').replace('ОБЩЕСТВО', 'О')
            os.rename(old_name, name_str)
    
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
