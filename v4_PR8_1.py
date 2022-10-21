from array import *
import math as m
import random as rnd

array1 = array('f', [])         # Створюємо 2 масиви
array2 = array('f', [])
N = int(input("Кільксть елементів у масиві: ")) # тримуємо значення змінних
L = int(input("Введть ліву межу значень: "))
R = int(input("Введть праву межу значень: "))

for i in range(N):              # Цикл, у якому заповнюютсья 2 масиви: 1ий - випадковими числами, 2ий - степенями 3.
    array1.append(rnd.randrange(L,R))
    array2.append(m.pow(3,i))

print (array1)
print (array2)

print(sorted(array1 + array2))


# Заєць Микита, практична №8, вар. 4, задача 1