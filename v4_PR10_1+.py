import re
import string
import os

os.chdir(r"F:\University\Python\PR_10")                         # Переходимо до папки проєкту


f = open ('freq.txt', 'w')                                      # Відчиняємо файли
doc_txt = open('text.txt', 'r')

freq = {}                                                  # Створюємо словник для запису слова та його частоти
text_string = doc_txt.read().lower()                            # Змінна, яка отримує весь текст, вирівняний
match_pattern = re.findall(r'\b[a-z]{1,25}\b', text_string)     # Змінна отримує слова, а не весь текст
 
for word in match_pattern:                  # Цикл, який рахує частоту слів
    count = freq.get(word,0)
    freq[word] = count + 1

freq_list = freq.keys()                # Змінна, яка отримує номер (частоту)
 
for words in freq_list:                     # Цикл, у якому записуємо данні у файл freq.txt
    f.write(str(freq[words]))
    f.write(" ")
    f.write(words)
    f.write("\n")

doc_txt.close()                             # Закриваємо файли для збереження змін
f.close()

#Практична робота 10, 1 задача, варіант 4, Заєць Микита, 16 група