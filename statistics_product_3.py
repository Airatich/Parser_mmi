# -*- coding: utf -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
from selenium.webdriver.common.keys import Keys
import re
import auth_data
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

url="https://old.metalsmining.ru/"
options=webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options)

YES_counter=[]
def auth():
    driver.get(url)
    input_login=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/form/div/input[1]")
    input_login.send_keys(auth_data.login_data)
    input_password = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[3]/form/div/input[2]")
    input_password.send_keys(auth_data.password_data)
    input_password.send_keys(Keys.RETURN)
    YES_counter.append("YES_auth")
    #print("YES_auth -- statistic_product")

def clicking_to_data():
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[1]/div/ul/li[2]/a").click()# Объемы
    YES_counter.append("YES_clicking_to_data")
    #print("YES_clicking_to_data -- statistic_product")

def clicking_all_statistics_product():
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div[2]/div/div[2]/span[4]/a").click() # Производство

    for i in range(1,4): ### Сырье прокат полуфабрикаты
        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
            (By.XPATH,
             f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[{str(i)}]/span"))).click()

    #клики cырье
    for i in range(1,8):
        time.sleep(1)
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[{str(i)}]/span[2]/input"))).click()


    #клики прокат
    for i in range(1,4):
        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[{str(i)}]/span[2]/input"))).click()

    #клики полуфабрикаты
    time.sleep(1)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[3]/ul/li/span[2]/input"))).click()
    YES_counter.append("YES_clicking_all_statistics_product")
    #print("YES_clicking_all_statistics_product -- statistic_product")

def show():
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/form/input[3]").click()
    YES_counter.append("YES_show")
    #print("YES_show -- statistic_product")

def param(month,year):
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[4]/select/option[2]"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH,f"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input[2]").clear()
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input[2]").send_keys(f"01.{month}.{year}")
    driver.find_element(By.XPATH,f"/html/body").click()

    time.sleep(1)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div/div/form/input"))).click()
    YES_counter.append("YES_param")
    #print("YES_param -- statistic_product")

def statistics_excel(month_inp, year_inp):
    time.sleep(10)
    source = driver.page_source
    soup = bs4.BeautifulSoup(source, "lxml")
    data = pd.read_html(str(soup))
    data = data[0]
    data.to_excel(rf"C:\Users\Админ\Documents\PyProjects\Parser_mmi\Excel\statistics_product_from_{month_inp.zfill(2)}.{year_inp}.xlsx", index=False)
    YES_counter.append("YES_statistics_excel")
    #print("YES_statistics_excel -- statistic_product")

def exit():
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/input").click()
    YES_counter.append("YES_exit")
    #print("YES_exit")

def main_product(month_inp, year_inp):
    time.sleep(3)
    start_time = time.time()

    try:
        auth()
    except Exception:
        print("problem with auth -- statistics_product")
    try:
        clicking_to_data()
    except Exception:
        print("problem with clicking_to_data -- statistics_product")
    try:
        clicking_all_statistics_product()
    except Exception:
        print("problem with clicking_all_statistics_product -- statistics_product")
    try:
        show()
    except Exception:
        print("problem with show -- statistics_product")
    if len(YES_counter)==4:
        try:
            param(month_inp.zfill(2),year_inp)
        except Exception:
            print("problem with param -- statistics_product")
        try:
            statistics_excel(month_inp, year_inp)
        except Exception:
            print("problem with statistics_excel -- statistics_product")
        if len(YES_counter) == 6:
            exit()
            print("third ready! -- statistics_product")
            print(
                f"Your file is named:\nstatistics_product_from_{month_inp.zfill(2)}.{year_inp}.xlsx\nTotal execution time: {time.time() - start_time} sec")

        else:
            exit()
            print("third -- error")

    else:
        print("Не прокликаны все кнопки -- statistics_product")
        try:
            exit()
        except Exception:
            print("problem with exit")



