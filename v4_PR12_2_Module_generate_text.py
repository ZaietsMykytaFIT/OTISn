import random as rnd

def phone_num_generator(M, N, abc):                 # Ф-ія
    array = []                                      # Пустий масив
    for i in range(M):
            array.append(rnd.choices(abc, k=N))     # До масиву додаємо випадкові знаки, довжиною N
    return(array)                                   # Повертає масив


#Практична робота 12, 2 модуль-задача, варіант 4, Заєць Микита, 16 група