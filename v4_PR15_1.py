import tkinter as tk        # Користувач задає межі діапазону.
import random as rnd        # Розробити програму, яка згенерує 8 випадкових чисел у цьому діапазоні і запише їх у файл,
import os                   # після чого виведе ці числа у віджет Text.
                            # Початкові параметри вікна: ширина – 250, висота – 400, колір тла – помаранчевий.
                            # Використати менеджер геометрії pack().

os.chdir(r"F:\University\Python\PR_15") # Раджу видалити під час перевірки.

def generator():
    L = int(entryL.get())
    R = int(entryR.get())
    x = []                                  # Список для збереження всіх чисел
    file = open ('rnd_num.txt', 'w')        # Відкриваємо файл для запису

    for i in range(8):                  # Цикл із 8 повторів
        num = rnd.randint(L,R)          # Генеруємо випадкове число в межах
        x.append(int(num))                   # Записуємо число у список всіх чисел
        file.write(str(num))            # Записуємо число у файл
        if i<7:                         # Перевірка для того, щоб створити 8 рядків, а не 9
            file.write("\n")            # Кожне число у файлі з нового рядка
    file.close                              # Закриваємо файл

    Text.delete('1.0', tk.END)
    Text.insert('1.0', str(x))


#main
win = tk.Tk()
win.geometry("250x400")
win.configure(bg='orange')
#text
Text = tk.Text(height = 8)
Text.insert('1.0', "Тут виведуться випадкові числа в діапазоні, записаному нижче")
Text.pack(expand=True, fill=tk.X, side=tk.TOP)
#text_input
entryL = tk.Entry(width=250)                            # Оскільки в умові не уточнено місце отриманння змінних,
entryL.insert(0, 'Введіть ліву межу')                   # я буду використовувати Entry
entryR = tk.Entry(width=250)
entryR.insert(0, 'Введіть праву межу')
entryL.pack()
entryR.pack()
#Бутон
Button0 = tk.Button(text="GO", height=5, command = generator)
Button0.pack(expand=1, fill=tk.X, side=tk.BOTTOM)

win.mainloop()

#Практична робота 15, 1 задача, варіант 4, Заєць Микита, 16 група