from operator import index
from re import S


Sl = {}
Ind = 0

for i in range(9):            # Цикл для вводу значень
    print("Введіть назву ", (i+1), "-го метлау: ")
    Name = str(input())
    print("Введіть густину ", Name)
    Index = float(input())
    Sl[Name] = Index            # Додаємозначення в словник
    if i==4:                    # 9 не ділиться націло на 2, тому тут ми отримуємо текстове значення, щоб потім вивести
        ind = Name

print("Оригінальний словник: ", Sl)
print("Сортований за назвами словник: ", sorted((key, value) for (key, value) in Sl.items()))   # Сортування за назвою, виводимо обизва значення
print("Сортований за густиною словник: ", sorted(Sl.items()))   # частина "reversed = True" не працює
print("Центральне значення словнкиа =", ind, Sl[ind])

#Практична робота 9, 3 задача, варіант 4, Заєць Микита, 16 група