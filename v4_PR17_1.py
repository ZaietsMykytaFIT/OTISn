import pandas as pd     # Файл bike.csv містить таблицю значень – обсяг продажів велосипедів трьома приватними підприємцями за місяцями поточного року.
import numpy as np      # Написати програму, яка запише ці дані в об´єкт DataFrame,
import os               # обчислить середні продажі для кожного підприємцями і запише результат у файл average.csv.

os.chdir(r'F:\University\Python\PR_17')         # Тека з цільовими файлами

all= pd.read_csv('bike.csv', delimiter=';')     # Зчитуємо інформацію з файлу як DataFrame
head = list(all.columns)                        # Отримуємо всі "заголовки"
A_avg = all.mean(axis=0, numeric_only=True)     # Отримуємо список всіх середніх значень. numeric_only порекомендував VScode

f = open ('average.csv', 'w', encoding="UTF-8")     # Створюємо новий файл

for i in range(3):
    txt = head[i+1]                             # Отримуємо 1 значення заголовка,
    num = A_avg[i].round(2)                     # відповідне йому середнє значення
    w_txt = str(txt) + ";" + str(num) + "\n"    # Готуємо рядок для запису
    f.write(str(w_txt))

f.close

#Практична робота 17, 1 задача, варіант 4, Заєць Микита, 16 група