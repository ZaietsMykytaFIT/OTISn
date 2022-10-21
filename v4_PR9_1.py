x = int(input("Введіть число, якому будуть кранті числа кортежу: ")) # Кратність x
list = []        # Майбутній кортеж А 
ListMid = []     # Майбутній кортеж B
ListEnd = []     # Майбутній кортеж C
ListSta = []     # Майбутній кортеж D
y = 0

for i in range(20):      # Заповнюємо повний список числами, кратними x; 20 чисел
    y=(i+1)*x            # i+1 для початку відліку від 1 замість 0
    list.append(y)

ListMid.append(list[10])    # Список B отримує середні значення за індексом, бо в умові сказано, що всього 20 чисел
ListMid.append(list[11])

ListEnd.append(list[-3])    # Список C отримує останні значення з повного списку
ListEnd.append(list[-2])
ListEnd.append(list[-1])

ListSta.append(list[1])     # Список D отримує перші значення з повного списку
ListSta.append(list[2])
ListSta.append(list[3])
ListSta.append(list[4])

A = tuple(list)          # Списки стають кортежами
B = tuple(ListMid)
C = tuple(ListEnd)
D = tuple(ListSta)

print ("Кортеж A: ", A)     # Виводимо кортежі
print ("Кортеж B: ", B)
print ("Кортеж C: ", C)
print ("Кортеж D: ", D)                                         #Практична робота 9, 1 задача, варіант 4, Заєць Микита, 16 група