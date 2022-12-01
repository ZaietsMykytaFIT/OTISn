import numpy as np              # Зобразити графік функції 𝑦=0,5𝑥+0,1𝑥ସ, 𝑥∈[−3;9],
import matplotlib.pyplot as plt # тип лінії – пунктирна, колір лінії – чорний. Зберегти графік у файл gr_file.tiff.


x = np.linspace(-3, 9, 128)
y = 0.5*x+0.1*(x**4)

plt.plot(x, y, 'k:', label='0,5x+0,1x^4')

plt.axis([-3, 9, -3, 9]) # задання [xmin, xmax, ymin, ymax]

plt.xlabel('x') # позначення осі абсцис
plt.ylabel('y') # позначення осі ординат
plt.title('0,5x+0,1x^4')    # назва графіка

plt.savefig('gr_file.tiff', dpi=300)    # Збереження зображення
plt.show()      #виведення графіка на екран

#Практична робота 16, 1 задача, варіант 4, Заєць Микита, 16 група