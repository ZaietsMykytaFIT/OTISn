from ast import Break
import math as m

#Практична робота 6, 3 задача, варіант 4, Заєць Микита, 16 група

l = float(input("Введіть ліву межу ф-ії: "))
r = float(input("Введіть праву межу ф-ії: "))
n = float(input("Введіть крок для x: "))    #Вводимо змінні

x = float(l)    # х, тобто змінна, починається з лівої межі
y = 0.0
spisok=[]       #Створюємо список
CLspisok=[]

while x<r:      #Цикл з післяумовою
    y = 7 - x*m.pow(m.e,2*x-1) + m.sqrt(m.fabs(x))
    y = round(y,1)                                  #Округлення до 1 числа після крапки
    spisok.append(y)
    x = x+n

print(spisok)
#for i in spisok: #Спроби зробити перевірку на повторювані величини
#    if spisok[i]==spisok[i+1]:
#        CLspisok+=spisok[i]
#set(CLspisok)
#print("Значення, що повторюються: ", CLspisok)