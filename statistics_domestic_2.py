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
options.add_argument("")

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
    #print("YES_auth")


def clicking_to_country():

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable( (By.XPATH,'/html/body/div[1]/div[3]/ul/li[3]/a'))).click() # Статистика
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div/div/div[1]/div/ul/li[2]/a"))).click()  # Объемы
    YES_counter.append("YES_clicking_to_country")
    #print("YES_clicking_to_country")

def clicking_statistics_domectic_consumers():

    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[2]/div/div[2]/span[3]/a").click()#Внутренние поставки

    #Потребители!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/span"))).click() #Потребители


    for i in range(1,4):   # KZ RU UA
        time.sleep(4)
        driver.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[{str(i)}]/span").click()

    # Тут категоря только сырье, прокликиваем в каждой стране:
    for i in range(1,4):
        time.sleep(1)
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[{str(i)}]/ul/li/span"))).click()
        # "/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[1]/ul/li/span"
        # "/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[2]/ul/li/span"

    # Клики продуктов КЗ
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[1]/ul/li/ul/li/span[2]/input"))).click()
    # Клики продуктов RU
    for i in range(1,7):
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[2]/ul/li/ul/li[{str(i)}]/span[2]/input"))).click()
    # Клики продуктов UK
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[3]/ul/li/ul/li/span[2]/input"))).click()
    YES_counter.append("YES_clicking_statistics_domectic_consumers")
    #print("YES_clicking_statistics_domectic_consumers")

def clicking_statistics_domectic_suppliers():
    # Поставщики!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/span"))).click()  # Поставщики
    time.sleep(4)
    for i in range(1, 4):  # KZ RU UA
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[{str(i)}]/span"))).click()



    # Клики категорий КЗ
    time.sleep(1)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[1]/ul/li/span"))).click()
    # Клики категорий Рос
    time.sleep(1)
    for i in range(1, 4):
        time.sleep(3)
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable(
            (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[2]/ul/li[{str(i)}]/span"))).click()
    # Клики категорий UK
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[3]/ul/li/span"))).click()



    # Клики продуктов КЗ
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[1]/ul/li/ul/li/span[2]/input"))).click()
    # driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[1]/ul/li/ul/li/span[2]/input").click()
    # Клики продуктов сырья RU
    time.sleep(3)
    for i in range(1, 7):
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[2]/ul/li[1]/ul/li[{str(i)}]/span[2]/input"))).click()
    # Клики продуктов проката RU
    time.sleep(3)
    for i in range(1, 4):
        time.sleep(1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[2]/ul/li[2]/ul/li[{str(i)}]/span[2]/input"))).click()
    # Клики продуктов пф RU
    time.sleep(3)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[2]/ul/li[3]/ul/li/span[2]/input"))).click()
    # Клики продуктов проката UK
    time.sleep(3)
    for i in range(1,4):
        time.sleep(1)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable(
            (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li[3]/ul/li/ul/li[{str(i)}]/span[2]/input"))).click()

    YES_counter.append("YES_clicking_statistics_domectic_suppliers")
    #print("YES_clicking_statistics_domectic_suppliers")




def show():
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/form/input[3]").click()
    time.sleep(3)
    YES_counter.append("YES_show")
    #print("YES_show")




def param(month,year):

    driver.find_element(By.XPATH,f"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input[2]").clear()
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input[2]").send_keys(f"01.{month}.{year}")
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[4]/select/option[2]"))).click()
    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div/div/form/input"))).click()
    time.sleep(5)
    YES_counter.append("YES_param")
    #print("YES_param")

def statistics_excel(month_inp, year_inp):
    time.sleep(3)

    # if len(YES_counter)==6:
    source = driver.page_source
    soup = bs4.BeautifulSoup(source, "lxml")
    data = pd.read_html(str(soup))
    data = data[0]
    data.to_excel(rf"C:\Users\Админ\Documents\PyProjects\Parser_mmi\Excel\statistics_domestic_from_{month_inp.zfill(2)}.{year_inp}.xlsx", index=False)
    time.sleep(3)
    YES_counter.append("YES_statistics_excel")
    #print("YES_statistics_excel")
    # else:
    #     print("Прожаты не все кнопки")


def exit():
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/input").click()
    YES_counter.append("YES_exit")
    #print("YES_exit")

def main_statistics_domestic(month_inp, year_inp):
    start_time=time.time()
    try:
        auth()
    except Exception:
        print("problem with auth -- statistics_domestic")

    try:
        clicking_to_country()
    except Exception:
        print("problem with clicking_to_country -- statistics_domestic")

    try:
        clicking_statistics_domectic_consumers()
    except Exception:
        print("problem with clicking_statistics_domectic_consumers -- statistics_domestic")
    try:
        clicking_statistics_domectic_suppliers()
    except Exception:
        print("problem with clicking_statistics_domectic_suppliers -- statistics_domestic")
    try:
        show()
    except Exception:
        print("problem with show -- statistics_domestic")
    if len(YES_counter)==5:
        try:
            param(month_inp.zfill(2),year_inp)
        except Exception:
            print("problem with param -- statistics_domestic")
        try:
            statistics_excel(month_inp, year_inp)
        except Exception:
            print("problem with statistics_excel -- statistics_domestic")

        if len(YES_counter) == 7:
            exit()
            print("second ready! -- statistics_domestic")
            print(
                f"Your file is named:\nstatistics_ex_im_CIS_from_{month_inp.zfill(2)}.{year_inp}.xlsx\nTotal execution time: {time.time() - start_time} sec")

        else:
            exit()
            print("second -- error")

    else:
        print("Не прокликаны все кнопки -- statistics_domestic")
        try:
            exit()
        except Exception:
            print("problem with exit")


