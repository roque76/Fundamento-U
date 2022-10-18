'''
Descripción: Realizar un programa capaz de calcular el peso de carga de una cantidad x de camiones.

Autor: John Jaime Madrid
Versión: 1.0
fecha: 06/10/2022


'''

i = 1
j = 0
carg = 0
pes_sac = 0

for i in range(20):
    print('Se introducira la capacidad del camion #', i, 'En KG')
    capacid = int(input('Ingresar valor de capacidad: '))

    while (carg+pes_sac)<= capacid:
        j = j+1
        print('Se ingresara el valor del peso de la saca #',j ,'en KG')
        pes_sac = float(input('Ingresar valor de peso: '))


        if pes_sac<0:
            print('Cargar la saca #', i)
            carg = carg + pes_sac
    if i<20:
        print('La carga sobrepasa la capacidad del camion #', i, 'Retire el exceso y comienze a cargar el camion #', i+1)

print('No cargar la saca. Despache camion #', i-1)
print('Fin de la carga del día')