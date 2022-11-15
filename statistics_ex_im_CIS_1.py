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


def clicking_to_data():
    driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/ul/li[3]/a').click()
    driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[1]/div/ul/li[2]/a").click()# Объемы
    YES_counter.append("YES_clicking_to_data")
    #print("YES_clicking_to_data")


def clicking_statistics_export():
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div[2]/div/div[2]/span[2]/a").click() #Статистика ЭК/ИМ СНГ

    #Экспорт!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/span").click() # Экспорт
    for i in range(1,4):   # RU UA KZ
        time.sleep(4)
        driver.find_element(By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[{str(i)}]/span").click()
    # Россия
    # клики категорий
    for i in range(1,4):
        time.sleep(2)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,f"""//*[@id="treeview"]/li[1]/ul/li[1]/ul/li[{str(i)}]/span"""))).click()

    #клики сырье
    for i in range(1,8):

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[1]/ul/li[1]/ul/li[{str(i)}]/span[2]/input"))).click()
    #клики прокат
    for i in range(1, 4):

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH,
             f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[1]/ul/li[2]/ul/li[{str(i)}]/span[2]/input"))).click()
    #клики полуфабрикаты

    for i in range(1, 4):

        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH,
             f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[1]/ul/li[3]/ul/li[{str(i)}]/span[2]/input"))).click()

    # Украина
    # клики категорий
    time.sleep(2)
    for i in range(1,4):
        time.sleep(1)
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,f"""//*[@id="treeview"]/li[1]/ul/li[2]/ul/li[{str(i)}]/span"""))).click()

    #клики сырье
    time.sleep(2)
    for i in range(1,3):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[2]/ul/li[1]/ul/li[{str(i)}]/span[2]/input"))).click()
    #клики прокат
    time.sleep(2)
    for i in range(1, 4):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH,
             f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[2]/ul/li[2]/ul/li[{str(i)}]/span[2]/input"))).click()

    #клики полуфабрикаты
    time.sleep(2)
    for i in range(1, 4):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH,
             f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[2]/ul/li[3]/ul/li[{str(i)}]/span[2]/input"))).click()

    # Казахстан
    # клики категорий (сырье)

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[3]/ul/li/span"))).click()
    # клики сырье
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[1]/ul/li[3]/ul/li/ul/li/span[2]/input"))).click()
    YES_counter.append("YES_clicking_statistics_export")
    #print("YES_clicking_statistics_export")

def clicking_statistics_import():

    # Импорт!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/span").click()  # Экспорт
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/span"))).click()

    # driver.find_element(By.XPATH,
                        # f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li/span").click() # RU
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li/span"))).click()


    # клики категорий
    time.sleep(3)
    for i in range(1, 4):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, f"""//*[@id="treeview"]/li[2]/ul/li/ul/li[{str(i)}]/span"""))).click()

    # клики сырье
    time.sleep(3)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li/ul/li[1]/ul/li/span[2]/input"))).click()

    # клики полуфабрикаты
    time.sleep(3)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li/ul/li[2]/ul/li/span[2]/input"))).click()

    # клики прокат
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/div/form/ul/li[2]/ul/li/ul/li[3]/ul/li/span[2]/input"))).click()
    YES_counter.append("YES_clicking_statistics_import")
    #print("YES_clicking_statistics_import")
def show():
    time.sleep(7)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/div/form/input[3]").click()
    YES_counter.append("YES_show")
    #print("YES_show")
def param(month,year):
    driver.find_element(By.XPATH,f"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input[2]").clear()
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[1]/input[2]").send_keys(f"01.{month}.{year}")
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,
         f"/html/body/div[2]/div[1]/div/div/form/div[2]/table/tbody/tr[2]/td[4]/select/option[2]"))).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div/div/form/input"))).click()
    time.sleep(5)
    YES_counter.append("YES_param")
    #print("YES_param")

def statistics_excel(month_inp, year_inp):
    time.sleep(2)

    source = driver.page_source
    soup = bs4.BeautifulSoup(source, "lxml")
    data = pd.read_html(str(soup))
    data = data[0]
    data.to_excel(rf"C:\Users\Админ\Documents\PyProjects\Parser_mmi\Excel\statistics_ex_im_CIS_from_{month_inp.zfill(2)}.{year_inp}.xlsx", index=False)
    YES_counter.append("YES_statistics_excel")
    #print("YES_statistics_excel")


def exit():
    driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[3]/input").click()
    YES_counter.append("YES_exit")
    #print("YES_exit")

def main_statistics_ex_im_CIS(month_inp, year_inp):
    start_time=time.time()
    try:
        auth()
    except Exception:
        print("problem with auth -- statistics_ex_im_CIS")
    try:
        clicking_to_data()
    except Exception:
        print("problem with clicking_to_data -- statistics_ex_im_CIS")
    try:
        clicking_statistics_export()
    except Exception:
        print("problem with clicking_statistics_export -- statistics_ex_im_CIS")
    try:
        clicking_statistics_import()
    except Exception:
        print("problem with clicking_statistics_import -- statistics_ex_im_CIS")
    try:
        show()
    except Exception:
        print("problem with show -- statistics_ex_im_CIS")
    if len(YES_counter)==5:

        try:
            param(month_inp.zfill(2),year_inp)
        except Exception:
            print("problem with param -- statistics_ex_im_CIS")
        try:
            statistics_excel(month_inp, year_inp)
        except Exception:
            print("problem with statistics_excel -- statistics_ex_im_CIS")

        if len(YES_counter) == 7:
            exit()
            print("first ready! -- statistics_ex_im_CIS")
            print(f"Your file is named:\nstatistics_ex_im_CIS_from_{month_inp.zfill(2)}.{year_inp}.xlsx\nTotal execution time: {time.time() - start_time} sec")
        else:
            exit()
            print("first -- error")
        # когда все готово
        # try:
        #     exit()
        #     if len(YES_counter)==8:
        #         print("YESS all right")
        #         print(f"fine!!!\nTotal execution time: {time.time() - start_time} sec")
        #     else:
        #         print("Something wrong :(")
        # except Exception:
        #     print("problem with exit")

    else:
        print("Не прокликаны все кнопки -- statistics_ex_im_CIS")
        try:
            exit()
        except Exception:
         print("problem with exit")




