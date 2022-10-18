'''
Descripción: Algoritmo capaz de calcular la media de notas de una cantidad x de estudiantes

Autor: John Jaime Madrid
Fecha:07/09/2022
Versión: 1.0
'''

acum1 = 0
num_alum = int(input('Ingrese la cantidad de alumnos a calificar: '))
n_mayor = 0
acum2 = 0

for x in range(num_alum):
  est_nom = str(input('Ingrese el nombre del alumno: '))
  print('Se ingresara la nota del alumno #', x)
  n = float(input('Ingrese el valor de la nota: . . .'))
  if n>=6:
    print('EL estudiante #',x, 'De nombre:',est_nom, 'Aprobo la nota.')
    acum2 = acum2+1
  else:
    print('EL estudiante #',x, 'De nombre:',est_nom,'Reprobo la nota.')
  acum1 = acum1+n

  if n>n_mayor:
    n_mayor = n
 
m=acum1/num_alum
print('La media de notas es de: ', m)
print(acum2, 'Estudiantes ganaron la materia')