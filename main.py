import time

from statistics_ex_im_CIS_1 import main_statistics_ex_im_CIS
import statistics_ex_im_CIS_1
from statistics_domestic_2 import main_statistics_domestic
from statistics_product_3 import main_product
from statistics_consumption_4 import main_consumption

def start():
    month_inp, year_inp = (input("Показать с: (номер месяца и год через пробел)\n")).split()
    print("Подожди 4 минутки, я уже приступил")
    start_time=time.time()
    main_statistics_ex_im_CIS(month_inp, year_inp)
    main_statistics_domestic(month_inp, year_inp)
    main_product(month_inp, year_inp)
    main_consumption(month_inp, year_inp)
    print(f"TOTAL TIME: {time.time()-start_time}")

start()
