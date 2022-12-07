import tkinter as tk        # Розробити екранний додаток, який перемикатиме колір при натисканні кнопки.
                            # Вікно програми повинно містити віджети: кнопка, три радіокнопки, фрейм.

def ch_white():                 # Як на мене, найлегший та найзрозуміліший спосіб змінювати колір
    UI.configure(bg="white")
def ch_black():
    UI.configure(bg="black")
def ch_green():
    UI.configure(bg="green")
def ch_orange():
    UI.configure(bg="orange")
    
# def next_color():                                 # Звичайна кнопка, яка мала змінювати колір на наступний
    # if color == tk.StringVar(value="white"):      # Не зміг реалізувати
        # n_color="black"                           # За умовою задачі необов'язково
        # UI.configure(bg=n_color)
    # elif color == tk.StringVar(value="black"):
        # n_color="green"
        # UI.configure(bg="n_color")
    # elif tk.StringVar(value="green"):
        # n_color="white"
        # UI.configure(bg="n_color")
    # Global color
    # color = n_color
    # або
    # color = tk.StringVar(value=n_color)


#main
UI = tk.Tk()
UI.geometry("240x320")
color = tk.StringVar(value="white")     # Переключення "кругляшка" вибору кольору. Взято із мережі інтернетт
#frame
frame = tk.Frame(master=UI, relief=tk.RAISED, borderwidth=5)

#radio_button
r_but1 = tk.Radiobutton(master = frame, text="Orange", command=ch_orange, value = "orange", variable=color)
r_but2 = tk.Radiobutton(master = frame, text="Black", command=ch_black, value = "black", variable=color)
r_but3 = tk.Radiobutton(master = frame, text="Green", command=ch_green, value = "green", variable=color)

#button
button=tk.Button(text = "Скинути колір до білого", command=ch_white)

#pack
frame.pack()
r_but1.pack()
r_but2.pack()
r_but3.pack()
button.pack()

UI.mainloop()

#Практична робота 15, 2 задача, варіант 4, Заєць Микита, 16 група