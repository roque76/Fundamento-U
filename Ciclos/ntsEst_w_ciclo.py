'''
Descripción: Leer de un estudiante su nombre y las notas de los tres parciales.

Se necesita calcular la nota definitiva, sabiendo que es el promedio de las notas de los parciales.

Adicionalmente, imprimir un mensaje, que indique si la nota es aprobada o no aprobada.


Autor: John Jaime Madrid
Fecha: 01/09/2022
Versión: 1.0
'''


#DECLARACIÓN DE VARIABLES/CAPTURA DE DATOS POR TECLADO

c_est=int(input('Ingresar cantidad de estudiantes: '))

for val_rep in range (c_est):
    
    c_grp=0
    print('Estudiante #', val_rep)
    nom= str(input('INGRESE EL NOMBRE DEL ESTUDIANTE: . . .'))
    n1= float(input('INGRESAR VALOR DE LA PRIMERA NOTA: . . .'))
    n2= float(input('INGRESAR VALOR DE LA SEGUNDA NOTA: . . .'))
    n3= float(input('INGRESAR VALOR DE LA TERCERA NOTA: . . .'))
    #PROCESOS
    n_def_prom= (n1+n2+n3)/3
    n_def_porc= (n1*0.25)+(n2*0.25)+(n3*0.5)
    #SALIDA POR PROMEDIO(CONDICIONAL)
    if (n_def_prom >= 3):
        print('La nota definitiva por promedio de:', nom, 'Es de:', n_def_prom, 'y esta aprobada.')
    else:
        print('La nota definitiva por promedio de:', nom, 'Es de:', n_def_prom, 'y esta reprobada.')
    #SALIDA POR PORCENTAJE(CONDICIONAL)
    if (n_def_prom >= 3):
        print('La nota definitiva por porcentaje de:', nom, 'Es de:', n_def_porc, 'y esta aprobada.')
    else:
        print('La nota definitiva por porcentaje de:', nom, 'Es de:', n_def_porc, 'y esta reprobada.')
    #Promedio grupo
    c_grp=c_grp+n_def_prom
pr_grc=c_grp/c_est

print(f'El promedio de notas del grupo es: {pr_grc}')
        