import os                       # Текстовий файл містить словник у форматі «ключ: значення»,
import matplotlib.pyplot as plt # ключами якого є назви продуктів, а значеннями – ціни цих продуктів.
import json                     # Програма повинна вивести на екран гістограму цін.

os.chdir(r"F:\University\Python\PR_16") #Папка з проєктом та фійлом dictionary.txt


counter1 = 0
counter2 = 0
x= []
y= []

with open('dictionary.txt') as f:   # Читаємо файл та отримуємо дані
    data = f.read()
d = json.loads(data)

for key in d:               # Цикл, де:
    x.append(counter1)      # до x дописується значення лічильника
    y.append(d[key])        # до y дописується значення зі словника
    counter1+= 1
    if d[key]>counter2:     # шукається верхня межа графіка
        counter2 = d[key]

plt.axis([-1, counter1, 0, int(counter2+counter2/65)])
#plt.hist(y, bins=x)                                    # Не працює. Причина для мене невідома
plt.bar(x,y)                                            # Тому виводиться інший тип діаграми, який в теоретичному матеріалі теж підписаний як гістограма
plt.show()

#Практична робота 16, 2 задача, варіант 4, Заєць Микита, 16 група