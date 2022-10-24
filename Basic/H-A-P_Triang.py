import math as m

c1= float(input('Ingresar valor de cateto: '))
c2= float(input('Ingresar valor de segundo cateto: '))

H=m.sqrt((pow(c1,2))+(pow(c2,2)))
A=(c1*c2)/2
P=c1+c2+H

print(f'El valor de la hipotenusa es: {H}')
print(f'El valor del area es de: {A}')
print(f'El valor del perimetro es de: {P}')