txt1 = input('Введіть текст: ').replace(',','').replace('!','').replace('?','') # Змінна тексту, в якій символи ,!? зникають
maxim = max(txt1.split(), key=len)  # Знаходимо найбільше слово за допомогою відповідної ф-ії
minim = min(txt1.split(), key=len)  # Те ж саме, але найменше 

print(txt1)                 # Виводимо фінальний текст, на всяк випадок
print(len(maxim))                   # Виводимо довжину найбільшого
print(len(minim))                   # та найменшого слова



# Заєць Микита, практична №7, вар. 4, задача 1