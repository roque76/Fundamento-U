
#Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que 
#se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos 
#por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido"""

#Fecha: 22/10/2022
#Autor: John Jaime Madrid

pr_t = int(input('Ingresar cantidad de preguntas: '))
pr_corr = int(input('Cantidad de respuestas correctas: '))
porc = (pr_corr*100)/pr_t

if porc >= 90:
    print('El usuario tiene un porcentaje de: ', porc,'Nivel maximo')
elif porc >=75:
    print('El usuario tiene un porcentaje de: ', porc,'Nivel medio')
elif porc >= 50:
    print('El usuario tiene un porcentaje de: ', porc,'Nivel regular')
else:
    print('El usuario tiene un porcentaje de: ', porc,'Fuera de nivel')