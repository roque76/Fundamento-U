cant_n=int(input('Ingresar cantidad de numeros: '))
x=int(input('Ingresar valor inicial: '))
for x in range(1,cant_n+1,1):
    cC_n=x*x
    ac_s=ac_s+cC_n
    print(f'El cuadrado de {x} es: {cC_n}')
print(f'La suma acumulada de los cuadrados es: {ac_s}')