import math as m

def funcMath(a):

    y = (m.cos(m.fabs(m.pow(a,3)-4)) + m.log(m.fabs(a),m.e)) / m.pow(a-8+m.pow(a,2),1/3)

    return(y)



x = float(input("Введіть x для цієї надскладної ф-ії: "))

y = funcMath(x)

print ("f(x) = ", y)