'''
Descripción: Realizar un programa que detecte los valores minimos y maximos de 
una lista de 100 numeros.

Autor: John Jaime Madrid
Fecha: 11/09/2022
Versión: 1.0
'''

num1 = int(input('Ingresar valor minimo: '))

val_max = num1
val_min = num1


for i in range(10):
  print('Ingresar valor número', i)
  num = int(input('Ingresar el valor del número: '))

  if num > val_max:
    print('Nuevo valor maximo ingresado')
    val_max = num
  if num < val_min:
    print('Nuevo valor minimo ingresado')
    val_min = num

print('VALOR MAXIMO:', val_max)
print('VALOR MINIMO:', val_min)