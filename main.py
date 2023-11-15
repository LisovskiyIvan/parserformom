import time
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import pandas as pd
from data import inns

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
driver = webdriver.Chrome(options=options)

try:
    # book = pd.read_excel("parserformom/test2.xlsx", usecols="b")
    # data = book.values.tolist()
    # for z in data:
    #     for i in z:
    for i in inns:
            driver.get("https://egrul.nalog.ru/index.html")
            
            input_id = driver.find_element(By.ID, "query")
            input_id.send_keys(i)
        
            search_btn = driver.find_element(By.ID, "btnSearch").click()
            time.sleep(1)
            get_btn = driver.find_element(By.CLASS_NAME, "btn-excerpt").click()
            time.sleep(2)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
