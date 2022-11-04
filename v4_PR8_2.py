import numpy as np          # Нарешті знайшов робочу інструкцію зі встановлення pip та numpy
import math as m


N = int(input("Введіть число N: "))             # Змінні
x = 0
counter = 0


if m.sqrt(N) - int(m.sqrt(N)) == 0:             # Якщо √N - цілий √N однакові
    n = int(m.sqrt(N))                              # корінь записується в змінну n без змін
    arrayN = np.eye(n)                              # та створюється порожній 2D масив розміром n на n

else:                                           # Якщо √N - цілий √N різні
    n = int(m.sqrt(N)) + 1                          # корінь + 1 записується в змінну n
    arrayN = np.eye(n)                              # та створюється порожній 2D масив розміром n на n


for i in range(n*n):                                # i - рахує числа для заповнення
    
    if counter == n:                                # перевірка рахувальника на кінець рядку масиву
        counter = 0                                 # скидання значення рахувальника
        x+=1                                        # перехід на наступний рядок
    
    arrayN[x,counter] = i+1                         # У масив з кординатою x, counter записується значення i+1, бо відлік від 1
    counter+=1                                      # Рахувальник рахує к-ть записаних значеннь на чьому рядку


print(arrayN)                                   # Виводимо масив


#Практична робота 8, 2 задача, варіант 4, Заєць Микита, 16 група