import random as rnd

def phone_num_generator(N):                                             # Функція
    num_operator = "099"                                                # Статичний оператор, тому без rnd
    num_list = []                                                       # Змінна для майбутнього списку номерів
    for i in range(N):
        num = num_operator + str(rnd.randint(1111111, 9999999))         # Генерація номерів
        num_list.append(num)                                            # Додання згенерованого номера до списку
    return (num_list)                                                   # Повернення списку до головного файлу


if __name__ == "__main__":                                              # Захист від безпосереднього запуску

    print("I feel that something wrong here...\n","Oh, I got it! this is module, not main part!\n","Let's find main file!")


#Практична робота 12, 1 модуль-задача, варіант 4, Заєць Микита, 16 група