import pandas as pd     # Файл points.json містить словник,
import numpy as np      # ключами якого є імена точок, а значеннями – координати цих точок на числовій прямій.
import os               # Написати програму, яка:
import json             # 1) зчитає дані й запише їх у масив Series, індексами якого будуть імена точок;
                        # 2) обчислить відстані між сусідніми точками і збережіть їх у файл len.json.

os.chdir(r'F:\University\Python\PR_17') # Гадаю, що вам вже знайома частина коду

f0 = open('points.json') # Відкриваємо файл
slovnik = json.load(f0)  # отримуємо словник

array = pd.Series(slovnik)  # Створюємо масив

counter = 0     # лічильники
first_time = 0
i1 = 0

length = len(slovnik)       # Довжина словника, для того, щоб не писати зайві ','
f1 = open ('len.json', 'w') # Відкриваємо 2-ий файл

f1.write("{")               # Перший запис JSON файлу
for keys in slovnik:        # Буде доволі складно розібратися
    if  counter%2 == 0:             # Якщо лічильник парний, виконується
        num1 = slovnik[keys]
        if first_time != 0:         # Прибираю проблему неініціалізованої змінної num2
            f1.write(", ")
            i1+=1
            totalnum = num1 - num2
            txt = '"'+str(i1)+'"'+': '+str(round(totalnum,2))   # Готується рядок за правилами JSON
            f1.write(txt)
        first_time=1
    else:                                                       # Те ж саме тут, але для непаврних
        if counter!=1 and counter!=length:                      # Ненаписання зайвих ','
            f1.write(", ")
        num2 = slovnik[keys]
        totalnum = num2 - num1
        i1+=1
        txt = '"'+str(i1)+'"'+': '+str(round(totalnum,2))
        f1.write(txt)
    counter += 1
f1.write("}")               # Останній запис JSON файлу

f0.close
f1.close

#Практична робота 17, 2 задача, варіант 4, Заєць Микита, 16 група