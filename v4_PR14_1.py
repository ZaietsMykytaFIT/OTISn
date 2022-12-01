import re                                       # Написати програму, яка підраховує кількість кожного з ключових слів на веб-сторінці.
from pip._vendor import requests                # Ключові слова задає користувач (у рядку), результат зберігається у форматі JSON.
from bs4 import BeautifulSoup # Файл повинен бути в одній папці з кодом 


KeyWords = input("Enter the keywords in the line (EN only):\n")     # Ввід ключових змінних
KeyWords = str.split(KeyWords)
req = requests.get("https://docs.unrealengine.com/5.1/en-US/unreal-engine-5.1-release-notes/")

if req.status_code != 200:      # Перевірка зв'язку з сайтом
    print("Error, no connection to this web")

WBS = BeautifulSoup(req.text,'html.parser')                 # 1\
WebText = WBS.find_all("p")                                 # 2--- Отримання тексту із сторінки (не впевнений що працює нормально)
WebText = re.findall(r'\b[a-z]{2,25}\b', str(WebText))      # 3/ (Приколад - слово Lumen, яке точно є в тексті. Чому - не можу зрозуміти)
f = open ('freq.JSON', 'w')
freq = {}
for word1 in WebText:                   # Цикл, який рахує частоту слів
    for word2 in KeyWords:              # 1---Порівняння слів із цільовими
        if word1 == word2:              # 2/
            count = freq.get(word1,0)
            freq[word2] = count + 1

freq_list = freq.keys()                     # Змінна, яка отримує номер (частоту)
 
for words in freq_list:                     # Цикл, у якому записуємо данні у файл freq.JSON
    f.write(words)
    f.write(" = ")
    f.write(str(freq[words]))
    f.write("\n")
f.close()
#Практична робота 14, 1 задача, варіант 4, Заєць Микита, 16 група