import random as rnd
import string

def phone_num_generator(M, N, abc):                 # Ф-ія
    array = []                                      # Пустий масив
    txt = ''
    Ftxt = ''
    for i in range(M):
        for ii in range(N):
            txt = rnd.choice(abc)                   # Створюємо випадкові знаки, кількістю N
            Ftxt += txt                             # Ще одна змінна для коректного додавання тексту до масиву
            if ii == N-1:
                array.append(Ftxt)                  # Додаємо знаки до масиву
                Ftxt = ''                           # Очищуємо буферну змінну для зберігання рядка

    return(array)                                   # Повертає масив


#Практична робота 12, 2 модуль-задача, варіант 4, Заєць Микита, 16 група