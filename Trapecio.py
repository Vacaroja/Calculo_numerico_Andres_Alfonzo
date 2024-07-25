""" 
f=funcion evaluada
a = valor de abajo de la integral
b= valor de arriba de la integral
n=numero de intervalos
h= el valor de subida entre cada intervalo
xcero=valor inicio
xuno=valor siguiente a xcero
"""


def trapecio (f,a,b,n):
    area=0
    h= (b - a) / n
    xcero= a
    for i in range(n):
        xuno=xcero+(i+1)*h
        area+=(h/2)*(f(xcero)+f(xuno))
        xcero=xuno
    return area
        
def imprimir_Riemann(f,a,b,n):
    print("--------------------------------------RIEMANN--------------------------------------")
    print("el valor aproximado a traves del metodo de Riemman es:",Riemann(f,a,b,n))
    print("--------------------------------------------------------------------------------------------")
    return Riemann(f,a,b,n)
    
    

    
