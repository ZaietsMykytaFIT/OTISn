import math as m

def funcMath_U(x,a,y):

    Z = (m.pow(x,3)+a)*(y-m.log(m.fabs(y),m.e)-m.sin(a))+m.pow(m.pow(x,3)+y,1/3)

    return(Z)



x = float(input("Введіть 1-шу змінну для ф-ії   (x): "))
a = float(input("Введіть 2-гу змінну для ф-ії (a): "))
y = float(input("Введіть 3-тю змінну для ф-ії   (y): "))

Z = funcMath_U(x,a,y)

print ("Z = ", Z)