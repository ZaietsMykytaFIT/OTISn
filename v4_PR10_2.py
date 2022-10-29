import os
from os import listdir

path = "F:/University/Python/PR_10/test_text"       # Шлях до цільових файлів
folder = os.listdir(path)                           # Змінна отримує назви та розширення файлів у папці

print(folder)                                       # Виводимо зміст папки

for item in folder:                                 # У циклі видаляємо файли з розширенням txt
    if item.endswith(".txt"):
        os.remove(os.path.join(path, item))

#Практична робота 10, 2 задача, варіант 4, Заєць Микита, 16 група